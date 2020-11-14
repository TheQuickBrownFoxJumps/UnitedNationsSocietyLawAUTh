from django.views.generic import TemplateView, ListView
from django.apps import apps

# Create your views here.


New = apps.get_model('news', 'New')
Event = apps.get_model('events', 'Event')


class HomeView(ListView):
    template_name = 'main/homepage.html'
    ordering = ['-date']

    def get_queryset(self):
        queryset = {
            'news': New.objects.all().order_by('-date'),
            'events': Event.objects.all().order_by('-date'),
        }
        return queryset

    def get_context_data(self, **kwargs):
        context = {
            'news': New.objects.all().order_by('-date'),
            'events': Event.objects.all().order_by('-date'),
        }
        return context


# class HomeView(ListView):
#     template_name = 'main/homepage.html'
#     context_object_name = 'news'
#     ordering = ['-date']
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         if query:
#             news = self.model.objects.filter(title__icontains=query)
#         else:
#             news = self.model.objects.all().order_by('-date')
#         return news


class AboutView(TemplateView):
    template_name = 'main/about_us.html'


class ContactView(TemplateView):
    template_name = 'main/contact.html'


class MembershipView(TemplateView):
    template_name = 'main/membership.html'
