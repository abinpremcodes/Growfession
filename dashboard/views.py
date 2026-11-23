
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Project, Task
from .forms import ProjectForm, TaskForm


@login_required
def developer_dashboard(request):
    return render(request, "dashboard/developer_dashboard.html")


@login_required
def recruiter_dashboard(request):
    return render(request, "dashboard/recruiter_dashboard.html")


@login_required
def mentor_dashboard(request):
    return render(request, "dashboard/mentor_dashboard.html")


# PROJECT VIEWS

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


@login_required
def project_edit(request, project_id):

    project = get_object_or_404(
        Project,
        id=project_id,
        user=request.user
    )

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect("project_list")

    else:
        form = ProjectForm(instance=project)

    return render(
        request,
        "dashboard/project_form.html",
        {
            "form": form,
            "project": project
        }
    )


@login_required
def project_delete(request, project_id):

    project = get_object_or_404(
        Project,
        id=project_id,
        user=request.user
    )

    if request.method == "POST":
        project.delete()

    return redirect("project_list")


# TASK VIEWS

@login_required
def task_list(request):

    tasks = Task.objects.filter(user=request.user)

    return render(
        request,
        "dashboard/task_list.html",
        {"tasks": tasks}
    )


@login_required
def task_create(request):

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            return redirect("task_list")

    else:
        form = TaskForm()

    return render(
        request,
        "dashboard/task_form.html",
        {"form": form}
    )


@login_required
def task_edit(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("task_list")

    else:
        form = TaskForm(instance=task)

    return render(
        request,
        "dashboard/task_form.html",
        {
            "form": form,
            "task": task
        }
    )


@login_required
def task_delete(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    if request.method == "POST":
        task.delete()

    return redirect("task_list")
