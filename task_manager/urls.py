from django.contrib import admin
from django.urls import path

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime

PENDING_TASKS = []
COMPLETED_TASKS = []

SERVER_START_TIME = datetime.datetime.now().strftime("%I:%M:%S %p %d-%b-%y")


def tasks_view(request):
    context = {"tasks": PENDING_TASKS, "time": SERVER_START_TIME}
    return render(request, "tasks.html", context)


def all_tasks_view(request):
    context = {"pending_tasks": PENDING_TASKS,
               "completed_tasks": COMPLETED_TASKS}
    return render(request, "all_tasks.html", context)


def add_task_view(request):
    new_task = request.GET.get("task")
    PENDING_TASKS.append(new_task)
    return HttpResponseRedirect("/tasks")


def delete_task_view(request, task_id):
    PENDING_TASKS.pop(task_id-1)
    return HttpResponseRedirect("/tasks")


def delete_completed_task_view(request, task_id):
    COMPLETED_TASKS.pop(task_id-1)
    return HttpResponseRedirect("/completed_tasks")


def mark_complete_task_view(request, task_id):
    task = PENDING_TASKS.pop(task_id-1)
    COMPLETED_TASKS.append(task)
    return HttpResponseRedirect("/tasks")


def completed_tasks_view(request):
    context = {"tasks": COMPLETED_TASKS, "time": SERVER_START_TIME}
    return render(request, "completed_tasks.html", context)


urlpatterns = [
    path("admin/", admin.site.urls),
    # Add all your views here
    path("tasks/", tasks_view),
    path("add-task/", add_task_view),
    path("delete-task/<int:task_id>/", delete_task_view),
    path("delete-task/completed/<int:task_id>/", delete_completed_task_view),
    path("complete_task/<int:task_id>/", mark_complete_task_view),
    path("completed_tasks/", completed_tasks_view),
    path("all_tasks/", all_tasks_view),
]
