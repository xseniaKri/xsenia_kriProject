from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, StatusViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'categories', StatusViewSet)


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('api/', include(router.urls)),
]