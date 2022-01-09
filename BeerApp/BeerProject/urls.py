from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import BeerProjectListView, BeerProjectView, BeerAddView, IngredientsAddView, MashTempAddView, \
    FermentationAddView, BoilVolumeAddView

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
    path('project/new/beer_boil_volume/', BoilVolumeAddView.as_view(), name='new_project_beer_boil_volume'),
    path('project/update/beer/<int:pk>/', views.update_beer_view, name='update_project_beer'),
    path('project/delete/beer/<int:pk>/', views.delete_beer_view, name='delete_project_beer'),
    path('project/update/ingredient/<int:pk>/', views.update_ingredients_view, name='update_ingredient'),
    path('project/delete/ingredient/<int:pk>/', views.delete_ingredients_view, name='delete_ingredient'),
    path('project/update/mashtemp/<int:pk>/', views.update_mashtemp_view, name='update_mashtemp'),
    path('project/delete/mashtemp/<int:pk>/', views.delete_mashtemp_view, name='delete_mashtemp'),
    path('project/update/fermentation/<int:pk>/', views.update_fermentation_view, name='update_fermentation'),
    path('project/delete/fermentation/<int:pk>/', views.delete_fermentation_view, name='delete_fermentation'),
    path('project/update/boil/<int:pk>/', views.update_boil_view, name='update_boil'),
    path('project/delete/boil/<int:pk>/', views.delete_boil_view, name='delete_boil'),
    path('project/update/image/<int:pk>/', views.update_image_view, name='update_image'),
    path('project/delete/image/<int:pk>/', views.delete_image_view, name='delete_image'),
]
