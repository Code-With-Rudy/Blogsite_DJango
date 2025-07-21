# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # existing paths from previous steps
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # New paths for CRUD
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'), # Added delete path
    path('register/', views.register, name='register'),
]