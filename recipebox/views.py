from django.shortcuts import render
from recipebox.models import Recipe, Author

def index(request):

    html = "index.html"

    recipes = Recipe.objects.all()

    return render(request, html, {'recipes': recipes})

def recipe_details(request, key):

    recipes = Recipe.objects.get(id=key)

    return render(request, 'recipe_details.html', {'recipes': recipes})

