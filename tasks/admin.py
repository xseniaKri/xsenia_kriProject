from django.contrib import admin
from .models import Task, Status

from django.contrib import admin
from .models import Task, Status

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'status',) # Показать эти поля в списке

class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Регистрация с кастомными классами
admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)