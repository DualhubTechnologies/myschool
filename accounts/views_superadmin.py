from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render, redirect
from accounts.models import User, Role, UserRole
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.mail import send_mail



# only super admin user can access this view
def is_super_admin(user):
    return user.is_superuser


@user_passes_test(is_super_admin)
def superadmin_dashboard(request):
    return render(request, "superadmin/dashboard.html")