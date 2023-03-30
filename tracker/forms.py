from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from tracker.models import Redactor, Newspaper, Topic


class RedactorForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "years_of_experience")


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    topic = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    text = {"placeholder": "YYYY-MM-DD"}
    publish_date = forms.DateField(widget=forms.TextInput(attrs=text))

    class Meta:
        model = Newspaper
        fields = "__all__"


class SearchForm(forms.Form):
    text = {"placeholder": "press Enter for searching"}
    search_text = forms.CharField(max_length=63,
                                  required=False,
                                  label="",
                                  widget=forms.TextInput(attrs=text))


