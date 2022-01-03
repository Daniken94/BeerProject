from django.urls import path
from . import views
from .views import OneBeerView, OneTypeView, list_of_beers

app_name = 'punkapi'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('beers_type/', views.list_of_beers_type, name='beers_type'),
    path('beers_type/page2', views.list_of_beers_type_page2, name='beers_type_page2'),
    path('beers_type/page3', views.list_of_beers_type_page3, name='beers_type_page3'),
    path('beers_type/page4', views.list_of_beers_type_page4, name='beers_type_page4'),
    path('beers_type/page5', views.list_of_beers_type_page5, name='beers_type_page5'),
    path('beers/', list_of_beers.as_view(), name='beers'),
    path('beers/page2', views.list_of_beers_page2, name='beers_page2'),
    path('beers/page3', views.list_of_beers_page3, name='beers_page3'),
    path('beers/page4', views.list_of_beers_page4, name='beers_page4'),
    path('beers/page5', views.list_of_beers_page5, name='beers_page5'),
    path('beer/<int:id>/', OneBeerView.as_view(), name='beer'),
    path('type/<int:id>/', OneTypeView.as_view(), name='type'),
]