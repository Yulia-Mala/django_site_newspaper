from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from .forms import RedactorForm
from .models import Topic, Newspaper, Redactor


def index(request):
    context = {

    }
    return render(request, "tracker/index.html", context=context)


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic

    def get_queryset(self):
        queryset = Topic.objects.all()
        return queryset.annotate(num_papers=Count("newspapers")).order_by("-num_papers")


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = ["name"]

    def get_success_url(self):
        return reverse("tracker:topic-detail", kwargs={"pk": self.object.pk})


class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = ["name"]

    def get_success_url(self):
        return reverse("tracker:topic-detail", kwargs={"pk": self.object.pk})


class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("tracker:topic-list")


class NewspaperCreateView(generic.CreateView):
    model = Newspaper
    fields = "__all__"

    def get_success_url(self):
        return reverse("tracker:newspaper-detail", kwargs={"pk": self.object.pk})


class NewspaperUpdateView(generic.UpdateView):
    model = Newspaper
    fields = "__all__"

    def get_success_url(self):
        return reverse("tracker:newspaper-detail", kwargs={"pk": self.object.pk})


class NewspaperDeleteView(generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("tracker:newspaper-list")


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorForm

    def get_success_url(self):
        return reverse("tracker:redactor-detail", kwargs={"pk": self.object.pk})


class RedactorUpdateView(generic.UpdateView):
    model = Redactor
    form_class = RedactorForm

    def get_success_url(self):
        return reverse("tracker:redactor-detail", kwargs={"pk": self.object.pk})








