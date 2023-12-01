# from django.shortcuts import render
from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "login.html"

class TopView(generic.TemplateView):
    template_name = "top.html"