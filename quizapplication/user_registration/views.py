from django.shortcuts import render
from .forms import UserForm, UserInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
"""This function renders homepage"""
def index(request):
    return render(request, "user_registration/index.html")


"""This function registers the user."""
def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            info = info_form.save(commit=False)  # Shanka
            info.user = user

            if "profile_image" in request.FILES:
                info.profile_image = request.FILES["profile_image"]

            info.save()

            registered = True

        else:
            print(user_form.errors, info_form.errors)
    else:
        user_form = UserForm()
        info_form = UserInfoForm()

    return render(
        request,
        "user_registration/register.html",
        {"user_form": user_form, "info_form": info_form, "registered": registered},
    )


"""This function logs in"""
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("user_registration:index"))
            else:
                return HttpResponse("Account is not active")
        else:
            return HttpResponse("Invalid login detail.")
    else:
        return render(request, "user_registration/login.html")


"""This function logs out"""
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user_registration:index"))