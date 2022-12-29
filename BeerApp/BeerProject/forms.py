from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django.contrib.auth.models import User
from .models import Beer, Ingredients, MashTemp, Fermentation, BoilVolume
from . import models


class AddBeerForm(ModelForm):
    class Meta:
        model = Beer
        fields = ["brew", "brew_date", "name", "tagline", "description", "og", "fg", "ibu", "ebc", "ph",
                  "beer_volume", "unit", "preparation_time", "boiling_time" , "bootled_date", "beer_image"]


# funkcja def __init__ służy do odfiltrowania pola select w formularzu po id usera
class AddBeerIngredientsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields['beer'].queryset = Beer.objects.filter(user=user)

    class Meta:
        model = Ingredients
        fields = ["name", "concern", "type", "description", "value", "unit", "ebc", "purpose", "aac", "country", "sequence",
                  "sequence_unit", "beer"]


class AddBeerBoilVolumeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields['beer'].queryset = Beer.objects.filter(user=user)

    class Meta:
        model = BoilVolume
        fields = ["value", "unit", "substance", "beer"]


class AddBeerMashTempForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields['beer'].queryset = Beer.objects.filter(user=user)

    class Meta:
        model = MashTemp
        fields = ["value_temperature", "unit", "duration", "sequence", "beer"]


class AddBeerFermentationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields['beer'].queryset = Beer.objects.filter(user=user)

    class Meta:
        model = Fermentation
        fields = ["value_temperature", "unit", "duration", "sequence", "beer"]