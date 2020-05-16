from django.views import generic
from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse

from .models import ImageData

def index(request):
    template_name = 'srgan/index.html'
    
    template = loader.get_template(template_name)

    return HttpResponse(template.render())