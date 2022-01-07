from django.urls import path
from . import views
from .views import BeerProjectListView, BeerProjectView, BeerAddView, IngredientsAddView, MashTempAddView, \
    FermentationAddView

app_name = 'beerproject'

urlpatterns = [
    path('projects/', BeerProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', BeerProjectView.as_view(), name='project'),
    path('project/new/', views.project_add_view, name='new_project'),
    path('project/new/beer/', BeerAddView.as_view(), name='new_project_beer'),
    path('project/new/beer_image/', views.beer_image_add_view, name='new_project_beer_image'),
    path('project/new/beer_ingredients/', IngredientsAddView.as_view(), name='new_project_beer_ingredients'),
    path('project/new/beer_mashtemp/', MashTempAddView.as_view(), name='new_project_beer_mashtemp'),
    path('project/new/beer_fermentation/', FermentationAddView.as_view(), name='new_project_beer_fermentation'),
]
