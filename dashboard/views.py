
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def developer_dashboard(request):
    return render(request, "dashboard/developer_dashboard.html")


@login_required
def recruiter_dashboard(request):
    return render(request, "dashboard/recruiter_dashboard.html")


@login_required
def mentor_dashboard(request):
    return render(request, "dashboard/mentor_dashboard.html")

