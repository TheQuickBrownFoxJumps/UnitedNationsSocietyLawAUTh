from django.urls import path, include, re_path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.EventsView.as_view(), name='events-list'),
    path('<str:slug>', views.EventDetail.as_view(), name='events-detail'),
]