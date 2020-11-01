from django.urls import path, include, re_path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsView.as_view(), name='news-list'),
    path('<int:pk>/', views.NewDetail.as_view(), name='news-detail'),
]
