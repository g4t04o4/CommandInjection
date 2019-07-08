from django.urls import path
from . import views

urlpatterns = [
    path('', views.ping),
    path('post/', views.new_post),
]
