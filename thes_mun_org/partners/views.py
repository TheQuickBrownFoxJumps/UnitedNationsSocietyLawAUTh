from django.shortcuts import render
from .models import Partner, Supporter
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView, )


# Create your views here.

class PartnersView(ListView):
    template_name = 'partners/partners_list.html'
    model = Partner
    context_object_name = 'partners'
