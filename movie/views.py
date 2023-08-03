from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Juan Esteban'})

def about(request):
    return render(request, 'about.html', {'name': 'Juan Esteban', 'age': '19'})
