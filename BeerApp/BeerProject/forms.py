from django import forms
from BeerProject.models import BeerImage


class BeerImageForm(forms.ModelForm):
    class Meta:
        model = BeerImage
        fields = ("image",)
