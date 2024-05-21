from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='Home'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('stage_detail/<int:pk>/', views.stage_detail, name='stage_detail'),
    path('event_detail/<int:pk>/', views.event_detail, name='event_detail'),
    path('logement_detail/<int:pk>/', views.logement_detail, name='logement_detail'),
    path('transport_detail/<int:pk>/', views.transport_detail, name='transport_detail'),
]