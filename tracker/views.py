from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from .forms import RedactorForm, SearchForm, NewspaperForm
from .models import Topic, Newspaper, Redactor


def index(request):
    context = {

    }
    return render(request, "tracker/index.html", context=context)


class TopicListView(generic.ListView):
    model = Topic

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search_text = self.request.GET.get("search_text", "")
        text = {"search_text": search_text}
        context["search_form"] = SearchForm(initial=text)
        return context

    def get_queryset(self):
        queryset = Topic.objects.annotate(num_papers=Count("newspapers")).order_by("-num_papers")
        name = self.request.GET.get("search_text")
        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class TopicDetailView(generic.DetailView):
    model = Topic


class RedactorListView( generic.ListView):
    model = Redactor

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search_text = self.request.GET.get("search_text", "")
        text = {"search_text": search_text}
        context["search_form"] = SearchForm(initial=text)
        return context

    def get_queryset(self):
        queryset = Redactor.objects.all()
        username = self.request.GET.get("search_text")
        if username:
            return queryset.filter(username__icontains=username)
        return queryset


class RedactorDetailView( generic.DetailView):
    model = Redactor


class NewspaperListView( generic.ListView):
    model = Newspaper
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search_text = self.request.GET.get("search_text", "")
        text = {"search_text": search_text}
        context["search_form"] = SearchForm(initial=text)
        return context

    def get_queryset(self):
        queryset = Newspaper.objects.all()
        title = self.request.GET.get("search_text")
        if title:
            return queryset.filter(title__icontains=title)
        return queryset


class NewspaperDetailView( generic.DetailView):
    model = Newspaper


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = ["name"]

    def get_success_url(self):
        return reverse("tracker:topic-detail", kwargs={"pk": self.object.pk})


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = ["name"]

    def get_success_url(self):
        return reverse("tracker:topic-detail", kwargs={"pk": self.object.pk})


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("tracker:topic-list")


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm

    def get_success_url(self):
        return reverse("tracker:newspaper-detail", kwargs={"pk": self.object.pk})


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm

    def get_success_url(self):
        return reverse("tracker:newspaper-detail", kwargs={"pk": self.object.pk})


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("tracker:newspaper-list")


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorForm

    def get_success_url(self):
        return reverse("tracker:redactor-detail", kwargs={"pk": self.object.pk})


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorForm

    def get_success_url(self):
        return reverse("tracker:redactor-detail", kwargs={"pk": self.object.pk})


