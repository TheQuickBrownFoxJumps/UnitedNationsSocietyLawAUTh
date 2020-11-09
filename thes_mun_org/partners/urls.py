from django.urls import path, include, re_path
from . import views

app_name = 'partners'

urlpatterns = [
    path('', views.PartnersView.as_view(), name='partners-list'),
]
