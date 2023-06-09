from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from tracker.views import (
    index,
    TopicListView,
    TopicDetailView,
    RedactorListView,
    RedactorDetailView,
    NewspaperListView,
    NewspaperDetailView,
    TopicCreateView,
    NewspaperCreateView,
    TopicUpdateView,
    NewspaperUpdateView,
    TopicDeleteView,
    NewspaperDeleteView,
    RedactorCreateView,
    RedactorUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list"
     ),
    path(
        "topics/<int:pk>/",
        TopicDetailView.as_view(),
        name="topic-detail"
     ),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list"
     ),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail"
     ),
    path(
        "newspapers/",
        NewspaperListView.as_view(),
        name="newspaper-list"
     ),
    path(
         "newspapers/<int:pk>/",
         NewspaperDetailView.as_view(),
         name="newspaper-detail"
     ),
    path(
         "topics/create/",
         TopicCreateView.as_view(),
         name="topic-create"
     ),
    path(
        "newspapers/create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create"
    ),
    path(
        "topics/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update"
    ),
    path(
        "newspapers/<int:pk>/update/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update"
    ),
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),
    path(
        "newspapers/<int:pk>/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete"
    ),
    path(
        "redactors/create/",
        RedactorCreateView.as_view(),
        name="redactor-create"
    ),
    path(
        "redactors/<int:pk>/update/",
        RedactorUpdateView.as_view(),
        name="redactor-update"
    ),
]

urlpatterns += staticfiles_urlpatterns()

app_name = "tracker"
