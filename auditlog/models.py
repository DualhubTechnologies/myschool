import uuid
from django.conf import settings
from django.db import models


class ActivityLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Who
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

    # Snapshot identity (store EMAIL here for your system)
    username = models.CharField(max_length=255, blank=True, default="")

    # What/where
    action = models.CharField(max_length=100)  # request, auth.login, model.create, etc.
    path = models.CharField(max_length=255, blank=True, default="")
    method = models.CharField(max_length=10, blank=True, default="")
    status_code = models.IntegerField(null=True, blank=True)

    # Which computer (best practical identifiers)
    device_id = models.CharField(max_length=64, blank=True, default="")
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, default="")
    session_key = models.CharField(max_length=40, blank=True, default="")

    # Object tracking
    app_label = models.CharField(max_length=100, blank=True, default="")
    model = models.CharField(max_length=100, blank=True, default="")
    object_id = models.CharField(max_length=64, blank=True, default="")
    object_repr = models.CharField(max_length=255, blank=True, default="")

    extra = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["created_at"]),
            models.Index(fields=["action", "created_at"]),
            models.Index(fields=["user", "created_at"]),
            models.Index(fields=["device_id", "created_at"]),
        ]

    def __str__(self):
        return f"{self.created_at} {self.username} {self.action} {self.path}"
