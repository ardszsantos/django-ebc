from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]
