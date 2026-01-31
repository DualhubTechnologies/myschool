from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import ActivityLog
from .middleware import get_current_request, get_client_ip, user_identity


def _log_model_event(instance, action, created=False):
    request = get_current_request()

    user = None
    identity = ""
    device_id = ""
    ip = None
    ua = ""
    session_key = ""
    path = ""
    method = ""

    if request:
        user = request.user if request.user.is_authenticated else None
        identity = user_identity(user) if user else ""
        device_id = request.COOKIES.get("device_id", "")
        ip = get_client_ip(request)
        ua = request.META.get("HTTP_USER_AGENT", "")[:1000]
        session_key = getattr(request.session, "session_key", "") or ""
        path = request.path or ""
        method = request.method or ""

    meta = instance._meta
    ActivityLog.objects.create(
        user=user,
        username=identity,
        action=action,
        path=path,
        method=method,
        status_code=None,
        device_id=device_id,
        ip_address=ip,
        user_agent=ua,
        session_key=session_key,
        app_label=meta.app_label,
        model=meta.model_name,
        object_id=str(getattr(instance, "pk", "")),
        object_repr=str(instance)[:255],
        extra={"created": created},
    )


@receiver(post_save)
def audit_post_save(sender, instance, created, **kwargs):
    if sender == ActivityLog:
        return
    if sender._meta.app_label in ("admin", "sessions", "contenttypes", "auth"):
        return

    action = "model.create" if created else "model.update"
    _log_model_event(instance, action=action, created=created)


@receiver(post_delete)
def audit_post_delete(sender, instance, **kwargs):
    if sender == ActivityLog:
        return
    if sender._meta.app_label in ("admin", "sessions", "contenttypes", "auth"):
        return

    _log_model_event(instance, action="model.delete")
