from django.contrib import admin
from .models import Task, Status  # Импортируем модели

admin.site.register(Task)  # Регистрируем модель Task
admin.site.register(Status)  # Регистрируем модель Status