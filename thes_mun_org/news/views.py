from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import New
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView, )
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

# def news_home(request, template_name='news/index_news.html'):
#     return render(request, template_name, {'posts': New.objects.all(), 'title': 'News'})


class NewsView(ListView):
    template_name = 'news/news_list.html'
    model = New
    context_object_name = 'news'
    # to order the post from latest to oldest
    ordering = ['-date']
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            news = self.model.objects.filter(title__icontains=query)
        else:
            news = self.model.objects.all().order_by('-date')
        return news


class NewDetail(DetailView):
    template_name = 'news/news_detail.html'
    model = New
