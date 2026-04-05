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
)


app_name = "manager"

urlpatterns = [
    path("", index, name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
    path("tag/", TagListView.as_view(), name="tag_list"),
    path("tag/create/", TagCreateView.as_view(), name="tag_create"),
    path("tag/update/<int:pk>/", TagUpdateView.as_view(), name="tag_update"),
    path("tag/delete/<int:pk>/", TagDeleteView.as_view(), name="tag_delete"),
]
