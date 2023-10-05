from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from forms import TaskCreationForm
from todolist.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks.html"
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = (
            Task.objects.all()
            .order_by("is_done", "-datetime")
        )
        return queryset


class TagsListView(generic.ListView):
    model = Tag
    template_name = "tags.html"
    context_object_name = "tags"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "task_create_update.html"
    success_url = reverse_lazy("todolist:tasks")


def toggle_task(request: HttpRequest, pk: int):
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy("todolist:tasks"))


class TagListView(generic.ListView):
    model = Tag
    template_name = "tags.html"
    context_object_name = "tags"


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "tag_create_update.html"
    context_object_name = "tag"
    fields = "__all__"
    success_url = reverse_lazy("todolist:tags")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tag_confirm_delete.html"
    context_object_name = "tag"
    success_url = reverse_lazy("todolist:tags")


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "tag_create_update.html"
    success_url = reverse_lazy("todolist:tags")
    fields = "__all__"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "task_create_update.html"
    success_url = reverse_lazy("todolist:tasks")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("todolist:tasks")
