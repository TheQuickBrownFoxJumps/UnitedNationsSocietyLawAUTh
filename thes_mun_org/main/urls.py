from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about', views.AboutView.as_view(), name='about-us'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('membership', views.MembershipView.as_view(), name='membership'),
]
