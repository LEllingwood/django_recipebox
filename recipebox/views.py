from django.shortcuts import render, get_object_or_404
from recipebox.models import Recipe, Author

def index(request):

    html = "index.html"

    recipes = Recipe.objects.all()

    return render(request, html, {'recipes': recipes})

def recipe(request, key):

    recipes = Recipe.objects.get(id=key)
    html = "recipe.html"

    return render(request, html, {'recipes': recipes})

def author(request, key):

    authors = Author.objects.get(pk=key)
    recipes = Recipe.objects.filter(author=authors)
    book = {'authors': authors, 'recipes': recipes}
    html = "author.html"

    return render(request, html, book)


