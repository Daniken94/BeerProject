from django.urls import path
from . import views


app_name ='home'

urlpatterns = [
    path('', views.list_of_beers_type, name='beers_type'),
]