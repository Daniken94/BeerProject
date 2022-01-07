from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

from .models import BeerImage, Beer, Ingredients, MashTemp, Fermentation
from . import models


class AddBeerForm(ModelForm):
    class Meta:
        model = Beer
        fields = "__all__"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.helper = FormHelper
            self.helper.form_method = 'post'
            self.helper.layout = Layout(
                "__all__",
                Submit('submit', 'Submit')
            )


class AddBeerImageForm(ModelForm):
    class Meta:
        model = BeerImage
        fields = "__all__"


class AddBeerIngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = "__all__"


class AddBeerMashTempForm(ModelForm):
    class Meta:
        model = MashTemp
        fields = "__all__"


class AddBeerFermentationForm(ModelForm):
    class Meta:
        model = Fermentation
        fields = "__all__"
