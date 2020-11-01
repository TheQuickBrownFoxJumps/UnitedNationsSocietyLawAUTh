from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Journal
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


class JournalView(ListView):
    template_name = 'journal/journal_list.html'
    model = Journal
    context_object_name = 'journal'
    # to order the post from latest to oldest
    ordering = ['-date']
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            journal = self.model.objects.filter(title__icontains=query)
        else:
            journal = self.model.objects.all()
        return journal


class JournalDetail(DetailView):
    template_name = 'journal/journal_detail.html'
    model = Journal
