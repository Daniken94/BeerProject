from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import BeerProjectListView, BeerProjectView, BeerAddView, IngredientsAddView, MashTempAddView, \
    FermentationAddView, BoilVolumeAddView, ProjectAddView, UpdateBeerView, DeleteBeerView, \
    UpdateIngredientsView, DeleteIngredientsView, UpdateMashtempView, DeleteMashtempView, UpdateFermentationView, \
    DeleteFermentationView, UpdateBoilView, DeleteBoilView

app_name = 'beerproject'

urlpatterns = [
    path('projects/', BeerProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', BeerProjectView.as_view(), name='project'),
    path('project/new/', ProjectAddView.as_view(), name='new_project'),
    path('project/new/beer/', BeerAddView.as_view(), name='new_project_beer'),
    path('project/new/beer_ingredients/', IngredientsAddView.as_view(), name='new_project_beer_ingredients'),
    path('project/new/beer_mashtemp/', MashTempAddView.as_view(), name='new_project_beer_mashtemp'),
    path('project/new/beer_fermentation/', FermentationAddView.as_view(), name='new_project_beer_fermentation'),
    path('project/new/beer_boil_volume/', BoilVolumeAddView.as_view(), name='new_project_beer_boil_volume'),
    path('project/update/beer/<int:pk>/', UpdateBeerView.as_view(), name='update_project_beer'),
    path('project/delete/beer/<int:pk>/', DeleteBeerView.as_view(), name='delete_project_beer'),
    path('project/update/ingredient/<int:pk>/', UpdateIngredientsView.as_view(), name='update_ingredient'),
    path('project/delete/ingredient/<int:pk>/', DeleteIngredientsView.as_view(), name='delete_ingredient'),
    path('project/update/mashtemp/<int:pk>/', UpdateMashtempView.as_view(), name='update_mashtemp'),
    path('project/delete/mashtemp/<int:pk>/', DeleteMashtempView.as_view(), name='delete_mashtemp'),
    path('project/update/fermentation/<int:pk>/', UpdateFermentationView.as_view(), name='update_fermentation'),
    path('project/delete/fermentation/<int:pk>/', DeleteFermentationView.as_view(), name='delete_fermentation'),
    path('project/update/boil/<int:pk>/', UpdateBoilView.as_view(), name='update_boil'),
    path('project/delete/boil/<int:pk>/', DeleteBoilView.as_view(), name='delete_boil'),
]
