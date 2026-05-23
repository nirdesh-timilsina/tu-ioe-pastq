from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subject/<str:subject_code>/', views.subject_detail, name='subject_detail'),
]