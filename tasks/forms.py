from django import forms
from django.template.defaultfilters import title
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to', 'status']
        labels = {
            'title':'Заголовок',
            'description':'Описание задачи',
            'due_date':'Выполнить до',
            'assigned_to':'Над задачей работает',
            'status':'Статус'
        }
        widgets = {
            'due_date': forms.TextInput(attrs={'id': 'id_due_date'}),
        }
