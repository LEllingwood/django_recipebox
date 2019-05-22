from django import forms
from recipebox.models import Author

class RecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=50)
    instructions = forms.CharField(widget=forms.Textarea)

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=75)
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=75)
    password = forms.CharField(widget=forms.PasswordInput())
    bio = forms.CharField(widget=forms.Textarea)

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=75)
    password = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())