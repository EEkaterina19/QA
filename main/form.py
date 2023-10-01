from .models import Task 
from django.forms import ModelForm, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        filds = ["title", "task", "cart"]
        widgets = {"title": TextInput(attrs={

            "class": 'form-conterl',

            "placeholder": 'Введите название'

        })}