from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('npos/', views.npos_index, name='npos_index'),
  path('npos/<int:npo_id>/', views.npos_detail, name='npos_detail'),
  path('npos/create/', views.NPOCreate.as_view(), name='npos_create'),
  path('npos/<int:pk>/update/', views.NPOUpdate.as_view(), name='npos_update'),
  path('npos/<int:pk>/delete/', views.NPODelete.as_view(), name='npos_delete'),
  path('npos/<int:npo_id>/add_event/', views.add_event, name='add_event'),
  path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  
]