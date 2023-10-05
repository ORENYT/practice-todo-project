import datetime

from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms import widgets, DateTimeInput

from todolist.models import Task, Tag


class TaskCreationForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["deadline"].required = False
        self.fields["tags"].required = False

    class Meta:
        model = Task
        fields = "__all__"
