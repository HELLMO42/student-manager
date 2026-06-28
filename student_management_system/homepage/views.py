from django.shortcuts import render
from django.template import loader
from .models import Test
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def test(request):
  content = Test.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'test': content,
    'pageContent': 'content/courseHome.html'
  }
  return HttpResponse(template.render(context, request))

def landing(request):
  return redirect('dashboard')

def dashboard(request):
  template = loader.get_template('index.html')
  context = {
    'pageHeader': 'headers/dashboardHeader.html',
    'pageContent': 'content/dashboard.html'
  }
  return HttpResponse(template.render(context, request))

def coursePage(request, pageName):
  template = loader.get_template('index.html')
  context = {
    'pageHeader': 'headers/courseHeader.html',
    'pageContent': f'content/course{pageName}.html'
  }
  return HttpResponse(template.render(context, request))