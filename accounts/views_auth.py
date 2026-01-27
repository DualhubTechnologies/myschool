from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.urls import reverse
from .forms import  StyledAuthForm
from django.contrib.auth import logout



@login_required
def user_dashboard(request):

    user = request.user

    return render(request, "user/dashboard.html", {
        "user": user,
    }) 

def logout_view(request):
    logout(request)
    return redirect("accounts:user_login")


@login_required
def force_password_change(request):
    user = request.user

    if request.method == "GET":
        return render(request, "auth/force_password_change.html")

    new_password = request.POST.get("password")

    if not new_password:
        messages.error(request, "Password cannot be empty.")
        return redirect("accounts:force_password_change")

    # Update password
    user.set_password(new_password)
    user.must_change_password = False
    user.save()

    # re-login user (needed because password changed)
    login(request, user)

    messages.success(request, "Password updated successfully.")
    return redirect("accounts:user_dashboard")



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from accounts.forms import StyledAuthForm

from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    form = StyledAuthForm(request, data=request.POST or None)

    if request.method == "GET":
        return render(request, "auth/login.html", {"form": form})

    if form.is_valid():
        email = form.cleaned_data["username"]   # email lives here
        password = form.cleaned_data["password"]

        user = authenticate(
            request,
            username=email,   # 🔑 THIS WAS THE BUG
            password=password
        )

        if user is None:
            messages.error(request, "Invalid email or password.")
            return redirect("accounts:user_login")

        login(request, user)

        # Force password change
        if user.must_change_password:
            return redirect("accounts:force_password_change")

        return redirect("accounts:user_dashboard")

    return render(request, "auth/login.html", {"form": form})
