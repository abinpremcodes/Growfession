
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Project
from .forms import ProjectForm


@login_required
def developer_dashboard(request):
    return render(request, "dashboard/developer_dashboard.html")


@login_required
def recruiter_dashboard(request):
    return render(request, "dashboard/recruiter_dashboard.html")


@login_required
def mentor_dashboard(request):
    return render(request, "dashboard/mentor_dashboard.html")


@login_required
def project_list(request):
    projects = Project.objects.filter(user=request.user)

    return render(
        request,
        "dashboard/project_list.html",
        {"projects": projects}
    )


@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()

            return redirect("project_list")

    else:
        form = ProjectForm()

    return render(
        request,
        "dashboard/project_form.html",
        {"form": form}
    )
