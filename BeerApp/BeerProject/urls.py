from django.urls import path
from . import views
from .views import BeerProjectListView, BeerProjectView

app_name = 'beerproject'

urlpatterns = [
    path('projects/', BeerProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', BeerProjectView.as_view(), name='project'),
]