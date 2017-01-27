from django.shortcuts import render
from django.views import generic
from .models import Page, Preferences

# Create your views here.

class ShowView(generic.DetailView):
    model = Page
    template_name = 'pages/show.html'
    slug_field = 'slug'

class HomepageView(generic.DetailView):
    model = Page
    template_name = 'pages/show.html'

    def get_object(self):
        return Preferences.objects.first().homepage
