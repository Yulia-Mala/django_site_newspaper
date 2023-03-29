from django.shortcuts import render
from django.views import generic
from .models import AUTH_USER_MODEL, Topic, Newspaper, Redactor


def index(request):
    context = {

    }
    return render(request, "tracker/index.html", context=context)


class TopicListView(generic.ListView):
    model = Topic


class TopicDetailView(generic.DetailView):
    model = Topic


class RedactorListView(generic.ListView):
    model = Redactor


class RedactorDetailView(generic.DetailView):
    model = Redactor


class NewspaperListView(generic.ListView):
    model = Newspaper


class NewspaperDetailView(generic.DetailView):
    model = Newspaper
