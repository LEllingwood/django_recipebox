from django.shortcuts import render, HttpResponseRedirect
from recipebox.models import Recipe, Author
from recipebox.forms import RecipeForm, AuthorForm, SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def homepage(request):
    html = "homepage.html"
    return render(request, html)


def index(request):

    html = "index.html"

    recipes = Recipe.objects.all()
    authors = Author.objects.all()

    return render(request, html, {'recipes': recipes, 'authors': authors})

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

@login_required()
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

@login_required()
def create_author(request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(data['name'], data['email'], data['password'])
            new_user.save()
            Author.objects.create(
                name=data['name'],
                user=new_user,
                bio=data['bio']
            )
            render(request, 'authorform.html')
            return HttpResponseRedirect('/thanks')
        else:
            form = AuthorForm()

        return render(request, 'authorform.html', {'form': form})


def create_user(request):
    global form
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(data['username'], data['email'], data['password'])
            new_user.save()
            login(request, new_user)
            render(request, 'signup.html')
            return HttpResponseRedirect('/index')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def dj_login(request):
    global form
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def dj_logout(request):
    logout(request)
    messages.info(request, 'You have successfully logged out')
    return HttpResponseRedirect('/')