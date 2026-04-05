from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from manager.models import Tag, Task

def index(request):
    return render(request, "manager/index.html")



class TaskCreateView(CreateView):
    model = Task
    success_url = reverse_lazy("manager:index")
    form_class = TaskForm

  
class TaskUpdateView(UpdateView):
    model = Task
    success_url = reverse_lazy("manager:index")
    form_class = TaskForm


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("manager:index")

  
class TagDetailView(DetailView):
    model = Tag


class TagCreateView(CreateView):
    model = Tag
    success_url = reverse_lazy("manager:tag_list.html")
    form_class = TagForm


class TagUpdateView(UpdateView):
    model = Tag
    success_url = reverse_lazy("manager:tag_list.html")
    form_class = TagForm


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("manager:index")