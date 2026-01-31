from django.contrib import admin
from .models import ActivityLog

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = (
        "created_at", "username", "action", "method", "status_code",
        "path", "ip_address", "device_id"
    )
    list_filter = ("action", "method", "status_code", "created_at")
    search_fields = ("username", "path", "device_id", "ip_address", "user_agent", "object_repr")
    ordering = ("-created_at",)
    readonly_fields = (
        "created_at", "user", "username", "action", "path", "method", "status_code",
        "device_id", "ip_address", "user_agent", "session_key",
        "app_label", "model", "object_id", "object_repr", "extra"
    )
