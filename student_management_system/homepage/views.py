from django.shortcuts import render
from django.template import loader
from .models import Test
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db import connection
from .forms import RegistrationForm, CourseForm

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
  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM course")
    courses = cursor.fetchall()
  context = {
    'pageHeader': 'headers/dashboardHeader.html',
    'pageContent': 'content/dashboard.html',
    'courses': courses,
    'form': CourseForm(),
  }
  return HttpResponse(template.render(context, request))

def coursePage(request, pageName):
  template = loader.get_template('index.html')
  context = {
    'pageHeader': 'headers/courseHeader.html',
    'pageContent': f'content/course{pageName}.html'
  }
  return HttpResponse(template.render(context, request))

def loginPage(request):
  template = loader.get_template('login.html')
  context = {
    'form': RegistrationForm()
  }
  if request.method=='POST':
    login(request)
    return redirect('dashboard')
  if request.method=='GET':
    getName(request)
  return HttpResponse(template.render(context, request))

def login(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(f"Received login credentials: {email}, {password}")
    return redirect('dashboard')

def getName(request):
  name = request.GET.get('name')
  if name:
    print(f"Received name: {name}")
    return HttpResponse(f"Hello, {name}!")
  return HttpResponse("Please provide a name.")

def hello_world(request):
  return HttpResponse("Hello World")

def scores(request):
  return HttpResponse("Scores Page")

def createCourse(request):
    print("createCourse called")
    print("Request method:", request.method)

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM course")
        courses = cursor.fetchall()

    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            print("Form is valid")
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']

            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO course (name, content) VALUES (%s, %s)",
                    [name, description]
                )

            # Stay on the same page
            return render(request, 'index.html', {
                'form': CourseForm(),
                'success': True,
                'pageHeader': 'headers/dashboardHeader.html',
                'pageContent': 'content/dashboard.html',
                'courses': courses,
            })

        # Form is invalid — render the same page with errors
        print("Form is invalid")
        print("Form errors:", form.errors)
        return render(request, 'index.html', {
            'form': form,
            'pageHeader': 'headers/dashboardHeader.html',
            'pageContent': 'content/dashboard.html',
            'courses': courses,
        })

    
