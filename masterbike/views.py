from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    context = {}
    temp = loader.get_template('masterbike\index.html')

    return HttpResponse(temp.render())