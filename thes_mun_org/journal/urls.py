from django.urls import path, include, re_path
from . import views

app_name = 'journal'

urlpatterns = [
    path('', views.JournalView.as_view(), name='journal-list'),
    path('<int:pk>/', views.JournalDetail.as_view(), name='journal-detail'),
]
