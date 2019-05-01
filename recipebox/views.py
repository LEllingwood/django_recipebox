from django.shortcuts import render, HttpResponseRedirect
from recipebox.models import Recipe, Author
from recipebox.forms import RecipeForm, AuthorForm



def index(request):

    html = "index.html"

    recipes = Recipe.objects.all()

    return render(request, html, {'recipes': recipes})

def thanks(request):

    html = 'thanks.html'

    return render(request, html)

def recipe(request, key):

    recipes = Recipe.objects.get(id=key)
    html = "recipe.html"

    return render(request, html, {'recipes': recipes})

def author(request, key):

    authors = Author.objects.get(id=key)
    recipes = Recipe.objects.filter(author=authors)
    book = {'authors': authors, 'recipes': recipes}
    html = "author.html"

    return render(request, html, book)

def post_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            render(request, 'recipeform.html')
            return HttpResponseRedirect('/thanks')
    else:
        form = RecipeForm()

    return render(request, 'recipeform.html', {'form': form})


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            render(request, 'authorform.html')
            return HttpResponseRedirect('/thanks')
    else:
        form = AuthorForm()

    return render(request, 'authorform.html', {'form': form})

