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
  return redirect('homepage')