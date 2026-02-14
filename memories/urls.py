from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_memory, name='add_memory'),
    path('memory/<int:pk>/', views.memory_detail, name='memory_detail'),
    path('memory/<int:pk>/edit/', views.edit_memory, name='edit_memory'),
    path('memory/<int:pk>/delete/', views.delete_memory, name='delete_memory'),
]
