from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Event
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
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

# def events_home(request, template_name='news/index_news.html'):
#     return render(request, template_name, {'posts': New.objects.all(), 'title': 'News'})


class EventsView(ListView):
    template_name = 'events/events_list.html'
    model = Event
    context_object_name = 'events'
    # to order the post from latest to oldest
    ordering = ['-date']
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            events = self.model.objects.filter(title__icontains=query)
        else:
            events = self.model.objects.all().order_by('-date')
        return events


class EventDetail(DetailView):
    template_name = 'events/events_detail.html'
    model = Event


