from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import (
     User, Role, Permission, RolePermission,
    UserRole, Invite, Session, AuditLog
)




# --- User ---
@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ("email", "full_name", "is_active", "is_staff", "last_login_at")
    list_filter = ("is_active", "is_staff")
    search_fields = ("email", "full_name")
    ordering = ("email",)


    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal", {"fields": ("full_name", "phone", "photo_url")}),
        ("Permissions", {"fields": (
            "is_active", "is_staff", "is_superuser", "groups", "user_permissions"
        )}),
        ("Important dates", {"fields": ("last_login_at", "created_at", "updated_at")}),
    )

    readonly_fields = ("last_login_at", "created_at", "updated_at")

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "full_name", "password1", "password2", "is_staff"),
        }),
    )


# --- Roles ---
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name","")


# --- Permissions ---
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("key", "description")
    search_fields = ("key",)


# --- Role Permissions ---
@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ("role", "permission", "assigned_by", "assigned_at")
    list_select_related = ("role", "permission", "assigned_by")


# --- User Roles ---
@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "assigned_by", "assigned_at")
    list_select_related = ("user", "role", "assigned_by")





# --- Session ---
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("user", "ip_address", "created_at", "last_seen_at")
    list_select_related = ("user", "")


# --- Audit Log ---
@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ("action", "actor", "created_at")
    search_fields = ("action", "actor__email")
    readonly_fields = ("before", "after", "actor", "action", "created_at")
    list_select_related = ("actor","")
