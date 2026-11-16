from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegistrationForm


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