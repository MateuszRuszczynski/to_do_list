from django.urls import path
from manager.views import (
    TagCreateView,
    TagDeleteView,
    TagListView,
    TagUpdateView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    index,
    toggle_task_done,
)


app_name = "manager"

urlpatterns = [
    path("", index, name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/toggle_done/<int:pk>/", toggle_task_done, name="toggle-task-done"),
    path("tag/", TagListView.as_view(), name="tag_list"),
    path("tag/create/", TagCreateView.as_view(), name="tag_create"),
    path("tag/update/<int:pk>/", TagUpdateView.as_view(), name="tag_update"),
    path("tag/delete/<int:pk>/", TagDeleteView.as_view(), name="tag_delete"),
]
