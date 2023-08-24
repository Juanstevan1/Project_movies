from django.contrib import admin
from .models import Movie
from .models import Movie_upcoming

# Register your models here.
admin.site.register(Movie)
admin.site.register(Movie_upcoming)