from django.http import HttpResponseForbidden

def permission_required(key):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user

            if not user.is_authenticated:
                return HttpResponseForbidden("Not authenticated")

            if not user.has_permission(key):
                return HttpResponseForbidden("Permission denied")

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
