from django.urls import path
from . import views




urlpatterns = [
    path('', views.projects_list, name='projects_list'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
]