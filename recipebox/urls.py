"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipebox.views import index, recipe, author, post_recipe, \
    thanks, create_author, create_user, dj_login, homepage, dj_logout
from recipebox.models import Author, Recipe

admin.site.register(Author)
admin.site.register(Recipe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path('recipe/<int:key>/', recipe),
    path('author/<int:key>/', author),
    path('recipeform/', post_recipe),
    path('authorform/', create_author),
    path('thanks/', thanks),
    path('signup/', create_user),
    path('login/', dj_login),
    path('logout/', dj_logout)

]
