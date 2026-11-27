
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Project, Task, LearningGoal
from .forms import ProjectForm, TaskForm, LearningGoalForm


@login_required
def developer_dashboard(request):

    # Dashboard statistics
    projects_count = Project.objects.filter(
        user=request.user
    ).count()

    tasks_count = Task.objects.filter(
        user=request.user
    ).count()

    completed_tasks_count = Task.objects.filter(
        user=request.user,
        status=Task.Status.COMPLETED
    ).count()

    learning_goals_count = LearningGoal.objects.filter(
        user=request.user
    ).count()

    # Recent projects
    recent_projects = Project.objects.filter(
        user=request.user
    ).order_by("-updated_at")[:3]

    # Upcoming and unfinished tasks
    upcoming_tasks = Task.objects.filter(
        user=request.user
    ).exclude(
        status=Task.Status.COMPLETED
    ).order_by("due_date", "-created_at")[:5]

    # Recently updated learning goals
    learning_goals = LearningGoal.objects.filter(
        user=request.user
    ).order_by("-updated_at")[:3]

    context = {
        "projects_count": projects_count,
        "tasks_count": tasks_count,
        "completed_tasks_count": completed_tasks_count,
        "learning_goals_count": learning_goals_count,
        "recent_projects": recent_projects,
        "upcoming_tasks": upcoming_tasks,
        "learning_goals": learning_goals,
    }

    return render(
        request,
        "dashboard/developer_dashboard.html",
        context
    )


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

            messages.success(request, "Project created successfully!")
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
            messages.success(request, "Project updated successfully!")
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
        messages.success(request, "Project deleted successfully!")

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

            messages.success(request, "Task created successfully!")
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
            messages.success(request, "Task updated successfully!")
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
        messages.success(request, "Task deleted successfully!")

    return redirect("task_list")


# LEARNING GOAL VIEWS

@login_required
def learning_goal_list(request):
    goals = LearningGoal.objects.filter(user=request.user)

    return render(
        request,
        "dashboard/learning_goal_list.html",
        {"goals": goals}
    )


@login_required
def learning_goal_create(request):
    if request.method == "POST":
        form = LearningGoalForm(request.POST)

        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()

            messages.success(request, "Learning goal created successfully!")
            return redirect("learning_goal_list")

    else:
        form = LearningGoalForm()

    return render(
        request,
        "dashboard/learning_goal_form.html",
        {"form": form}
    )


@login_required
def learning_goal_edit(request, goal_id):
    goal = get_object_or_404(
        LearningGoal,
        id=goal_id,
        user=request.user
    )

    if request.method == "POST":
        form = LearningGoalForm(request.POST, instance=goal)

        if form.is_valid():
            form.save()
            messages.success(request, "Learning goal updated successfully!")
            return redirect("learning_goal_list")

    else:
        form = LearningGoalForm(instance=goal)

    return render(
        request,
        "dashboard/learning_goal_form.html",
        {
            "form": form,
            "goal": goal
        }
    )


@login_required
def learning_goal_delete(request, goal_id):
    goal = get_object_or_404(
        LearningGoal,
        id=goal_id,
        user=request.user
    )

    if request.method == "POST":
        goal.delete()
        messages.success(request, "Learning goal deleted successfully!")

    return redirect("learning_goal_list")
