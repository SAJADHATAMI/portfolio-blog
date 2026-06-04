from django.urls import path
from . import views






urlpatterns = [
    path('', views.courses_list, name='courses_list'),
    path('<slug:slug>/', views.course_detail, name='course_detail'),

]