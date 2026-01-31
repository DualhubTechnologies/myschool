import time
import uuid
import threading

_thread_locals = threading.local()

def get_current_request():
    return getattr(_thread_locals, "request", None)

def get_client_ip(request):
    xff = request.META.get("HTTP_X_FORWARDED_FOR")
    if xff:
        return xff.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


def user_identity(user):
    # Your system uses email as username
    return (
        getattr(user, "email", "")
        or getattr(user, "full_name", "")
        or str(getattr(user, "pk", ""))
    )


class CurrentRequestMiddleware:
    """
    Makes request accessible inside signals so we can know who changed models.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.request = request
        try:
            return self.get_response(request)
        finally:
            _thread_locals.request = None


class ActivityLogMiddleware:
    DEVICE_COOKIE_NAME = "device_id"

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()

        device_id = request.COOKIES.get(self.DEVICE_COOKIE_NAME)
        if not device_id:
            device_id = uuid.uuid4().hex

        response = self.get_response(request)

        path = request.path or ""
        if path.startswith("/static/") or path.startswith("/media/"):
            if self.DEVICE_COOKIE_NAME not in request.COOKIES:
                response.set_cookie(self.DEVICE_COOKIE_NAME, device_id, max_age=60*60*24*365*5)
            return response

        from .models import ActivityLog

        duration_ms = int((time.time() - start) * 1000)
        user = request.user if getattr(request, "user", None) and request.user.is_authenticated else None
        identity = user_identity(user) if user else ""

        try:
            ActivityLog.objects.create(
                user=user,
                username=identity,
                action="request",
                path=path,
                method=request.method or "",
                status_code=getattr(response, "status_code", None),
                device_id=device_id,
                ip_address=get_client_ip(request),
                user_agent=(request.META.get("HTTP_USER_AGENT", "")[:1000]),
                session_key=(getattr(request.session, "session_key", "") or ""),
                extra={
                    "duration_ms": duration_ms,
                    "query_string": request.META.get("QUERY_STRING", ""),
                    "referer": (request.META.get("HTTP_REFERER", "")[:1000]),
                },
            )
        except Exception:
            pass

        if self.DEVICE_COOKIE_NAME not in request.COOKIES:
            response.set_cookie(self.DEVICE_COOKIE_NAME, device_id, max_age=60*60*24*365*5)

        return response
