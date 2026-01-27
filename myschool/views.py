from django.shortcuts import render

def error_page(request, exception=None, status_code=500):
    messages = {
        400: "Bad request.",
        403: "You are not allowed to access this page.",
        404: "The page you requested was not found.",
        500: "An internal server error occurred.",
    }

    context = {
        "status_code": status_code,
        "message": messages.get(status_code, "An unexpected error occurred."),
    }

    return render(request, "error.html", context, status=status_code)
