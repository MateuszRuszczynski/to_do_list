from django import forms
from .models import Task, Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter tag name...",
                }
            ),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "What needs to be done?",
                }
            ),
            "deadline": forms.DateTimeInput(attrs={"type": "date"}),
            "tags": forms.CheckboxSelectMultiple(),
        }
