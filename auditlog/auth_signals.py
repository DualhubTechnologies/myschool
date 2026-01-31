from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

from .models import ActivityLog
from .middleware import get_client_ip


def user_identity(user):
    return getattr(user, "email", "") or getattr(user, "full_name", "") or str(getattr(user, "pk", ""))


@receiver(user_logged_in)
def on_login(sender, request, user, **kwargs):
    ActivityLog.objects.create(
        user=user,
        username=user_identity(user),   # stores email
        action="auth.login",
        path=request.path,
        method=request.method,
        device_id=request.COOKIES.get("device_id", ""),
        ip_address=get_client_ip(request),
        user_agent=request.META.get("HTTP_USER_AGENT", "")[:1000],
        session_key=getattr(request.session, "session_key", "") or "",
        extra={},
    )


@receiver(user_logged_out)
def on_logout(sender, request, user, **kwargs):
    ActivityLog.objects.create(
        user=user if getattr(user, "is_authenticated", False) else None,
        username=user_identity(user) if getattr(user, "is_authenticated", False) else "",
        action="auth.logout",
        path=request.path,
        method=request.method,
        device_id=request.COOKIES.get("device_id", ""),
        ip_address=get_client_ip(request),
        user_agent=request.META.get("HTTP_USER_AGENT", "")[:1000],
        session_key=getattr(request.session, "session_key", "") or "",
        extra={},
    )


@receiver(user_login_failed)
def on_login_failed(sender, credentials, request, **kwargs):
    if not request:
        return
    ActivityLog.objects.create(
        user=None,
        username=credentials.get("email", "") or credentials.get("username", "") or "",
        action="auth.login_failed",
        path=request.path,
        method=request.method,
        device_id=request.COOKIES.get("device_id", ""),
        ip_address=get_client_ip(request),
        user_agent=request.META.get("HTTP_USER_AGENT", "")[:1000],
        session_key=getattr(request.session, "session_key", "") or "",
        extra={},
    )
