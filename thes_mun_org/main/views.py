from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    template_name = 'main/homepage.html'


class AboutView(TemplateView):
    template_name = 'main/about_us.html'


class ContactView(TemplateView):
    template_name = 'main/contact.html'
