from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django.contrib.auth.models import User
from .models import BeerImage, Beer, Ingredients, MashTemp, Fermentation, BoilVolume
from . import models


class AddBeerForm(ModelForm):
    class Meta:
        model = Beer
        fields = "__all__"


class AddBeerImageForm(ModelForm):
    class Meta:
        model = BeerImage
        fields = "__all__"


class AddBeerIngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = "__all__"


class AddBeerBoilVolumeForm(ModelForm):
    class Meta:
        model = BoilVolume
        fields = "__all__"


class AddBeerMashTempForm(ModelForm):
    class Meta:
        model = MashTemp
        fields = "__all__"


class AddBeerFermentationForm(ModelForm):
    class Meta:
        model = Fermentation
        fields = "__all__"
