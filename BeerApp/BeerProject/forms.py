from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

from .models import BeerImage, Beer
from . import models


class BeerImageForm(ModelForm):
    class Meta:
        model = BeerImage
        fields = ("image",)


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
