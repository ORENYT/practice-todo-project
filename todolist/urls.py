from django.urls import path

from todolist.views import (
    TaskListView,
    TagsListView,
    TaskCreateView,
    toggle_task,
    TagUpdateView,
    TagDeleteView,
    TagCreateView,
    TaskDeleteView,
    TaskUpdateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks"),
    path("tags/", TagsListView.as_view(), name="tags"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("toggle/<int:pk>/", toggle_task, name="toggle"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag_update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag_delete"),
    path("tags/create/", TagCreateView.as_view(), name="tag_create"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
]

app_name = "todolist"
