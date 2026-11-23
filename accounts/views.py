
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .forms import RegistrationForm, DeveloperProfileForm
from .models import DeveloperProfile, User


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your Growfession account has been created successfully!"
            )
            return redirect("register")

    else:
        form = RegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                messages.success(
                    request,
                    "Welcome back to Growfession!"
                )
                return redirect("register")

    else:
        form = AuthenticationForm()

    return render(
        request,
        "accounts/login.html",
        {"form": form},
    )


@login_required
def developer_profile_view(request):

    if request.user.role != "DEVELOPER":
        return HttpResponseForbidden(
            "Only developer accounts can access this page."
        )

    profile, created = DeveloperProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        form = DeveloperProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            messages.success(
                request,
                "Your developer profile has been saved successfully!"
            )

            return redirect("developer_profile")

    else:
        form = DeveloperProfileForm(instance=profile)

    return render(
        request,
        "accounts/developer_profile.html",
        {"form": form, "profile": profile},
    )


def public_developer_profile_view(request, username):

    developer = get_object_or_404(
        User,
        username=username,
        role="DEVELOPER",
    )

    profile = get_object_or_404(
        DeveloperProfile,
        user=developer,
        is_public=True,
    )

    skills = [
        skill.strip()
        for skill in profile.skills.split(",")
        if skill.strip()
    ]

    return render(
        request,
        "accounts/public_developer_profile.html",
        {
            "developer": developer,
            "profile": profile,
            "skills": skills,
        },
    )
