from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from manager.forms import TagForm, TaskForm
from manager.models import Tag, Task


def index(request):
    tasks = Task.objects.prefetch_related("tags").order_by("is_done", "-datetime")
    return render(request, "manager/index.html", {"tasks": tasks})


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:index")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:index")
    success_url = reverse_lazy("manager:index")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("manager:index")


class TagListView(ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "manager/tag_list.html"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("manager:tag_list.html")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("manager:tag_list.html")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("manager:index")
