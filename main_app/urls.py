from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  # path('npos/', views.npos_index, name='npo_index')
]