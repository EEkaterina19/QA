from django.contrib import admin
from .models import Task
from django import forms
from django.core.exceptions import ValidationError



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = 'all'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and Task.objects.exists():
            raise ValidationError("Может быть создана только одна запись для Первая карточка топ блока")

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    form = TaskForm
    list_display = ['title', 'titleh1', 'button1', 'button2', 'updated']
    readonly_fields = ('created',)
    search_fields = ['updated']