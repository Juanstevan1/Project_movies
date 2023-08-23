from django.shortcuts import render
from .models import Movie
# Create your views here.
def home(request):
    searchTerm = request.GET.get('SearchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm1':searchTerm})

def about(request):
    return render(request, 'about.html', {'name': 'Juan Esteban', 'age': '19'})
