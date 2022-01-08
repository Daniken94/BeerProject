from django.urls import path
from . import views
from .views import AlcCalcView, AutCalcView, IBUCalcView, EBCCalcView

app_name = 'calculator'

urlpatterns = [
    path('alc/', AlcCalcView.as_view(), name='calc_alc'),
    path('aut/', AutCalcView.as_view(), name='calc_aut'),
    path('ibu/', IBUCalcView.as_view(), name='calc_ibu'),
    path('ebc/', EBCCalcView.as_view(), name='calc_ebc'),
]