from django.shortcuts import render
from django.views.generic import ListView
from .models import  Task,Task1,Task2,Task3

class AllModelsViews(ListView):
    template_name = 'main.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task1'] = Task1.objects.all()
        context['task2'] = Task2.objects.all()
        context['task3'] = Task3.objects.all()
        return context