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
    # choices = [(a.id, a.user.username) for a in Author.objects.all()]
    # user = forms.ChoiceField(choices=choices)
    bio = forms.CharField(widget=forms.Textarea)