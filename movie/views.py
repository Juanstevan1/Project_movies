from django.shortcuts import render

# Create your views here.

def home(request):
    searchTerm = request.GET.get('SearchMovie')
    return render(request, 'home.html', {'searchTerm1':searchTerm})

def about(request):
    return render(request, 'about.html', {'name': 'Juan Esteban', 'age': '19'})
