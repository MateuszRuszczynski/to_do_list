from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from manager.forms import TagForm, TaskForm
from manager.models import Tag, Task


def index(request):
    tasks = Task.objects.prefetch_related("tags").order_by("is_done", "-datetime")
    return render(request, "manager/index.html", {"tasks": tasks})


def toggle_task_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("manager:index")


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:index")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:index")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("manager:index")


class TagListView(ListView):
    model = Tag
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("manager:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("manager:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("manager:tag-list")
