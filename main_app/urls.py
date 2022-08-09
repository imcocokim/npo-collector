from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('npos/', views.npos_index, name='npos_index'),
  path('npos/<int:npo_id>', views.npos_detail, name='npos_detail'),
]