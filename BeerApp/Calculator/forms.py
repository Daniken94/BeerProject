from django.forms import ModelForm
from django import forms


class AlcCalcForm(forms.Form):
    OG = forms.FloatField(label="Initial density BLG")
    FG = forms.FloatField(label="Final density BLG")

class AutCalcForm(forms.Form):
    value_beer = forms.FloatField(label="Number of liters of finished beer")
    blg = forms.FloatField(label="Initial beer BLG")
    value_malt = forms.FloatField(label="Number of kg of malt")

class IBUCalcForm(forms.Form):
    hops = forms.FloatField(label="The weight of the hops")
    acids = forms.FloatField(label="% alfa acid in hops")
    utilization = forms.FloatField(initial='30', label="% hops utilization", help_text="Typical utilization is 30%")
    value_beer = forms.FloatField(label="Number of liters of finished beer")
