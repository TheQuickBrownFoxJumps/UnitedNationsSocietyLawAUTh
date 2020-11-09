from django.urls import path, include, re_path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.BoardView.as_view(), name='board-list'),
]