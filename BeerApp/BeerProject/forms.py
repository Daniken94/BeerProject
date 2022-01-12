from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django.contrib.auth.models import User
from .models import BeerImage, Beer, Ingredients, MashTemp, Fermentation, BoilVolume
from . import models


class AddBeerForm(ModelForm):
    class Meta:
        model = Beer
        # fields = "__all__"
        exclude = ["user"]


# funkcja def __init__ służy do odfiltrowania pola select w formularzu po id usera
class AddBeerImageForm(ModelForm):
    # beer = forms.ModelChoiceField(queryset=Beer.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields['beer'].queryset = Beer.objects.filter(user=user)

    class Meta:
        model = BeerImage
        fields = "__all__"


class AddBeerIngredientsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields['beer'].queryset = Beer.objects.filter(user=user)

    class Meta:
        model = Ingredients
        fields = "__all__"


class AddBeerBoilVolumeForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields['beer'].queryset = Beer.objects.filter(user=user)

    class Meta:
        model = BoilVolume
        fields = "__all__"


class AddBeerMashTempForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields['beer'].queryset = Beer.objects.filter(user=user)

    class Meta:
        model = MashTemp
        fields = "__all__"


class AddBeerFermentationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields['beer'].queryset = Beer.objects.filter(user=user)

    class Meta:
        model = Fermentation
        fields = "__all__"
