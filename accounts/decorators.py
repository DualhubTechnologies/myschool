from django.http import HttpResponseForbidden

def permission_required(key):
    """
    Decorator that checks if the logged-in user has a given permission.
    Usage: @permission_required("students.read")
    """

    def decorator(view_func):
        def _wrapped(request, *args, **kwargs):

            # User not logged in
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Not authenticated")

            # Check permission using your user.has_permission()
            if not request.user.has_permission(key):
                return HttpResponseForbidden("Permission denied")

            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator
