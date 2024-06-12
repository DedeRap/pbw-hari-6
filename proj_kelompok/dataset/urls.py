from django.urls import path
from . import views

urlpatterns = (
    path('', views.dataset_list, name='dataset_list'),
    path('create/', views.dataset_create, name='dataset_create'),
)