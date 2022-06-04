from django.test import TestCase
from .models import Beer, Ingredients, BoilVolume, MashTemp, Fermentation, BeerImage
from django.contrib.auth.models import User


# class BeerModelTestCase(TestCase):
#     def setUp(self):    #uruchomiona metoda przy każdym rozpoczęciu testów
#         self.beer = Beer(name="Atak Chmielu", tagline="IPA", beer_volume="20", unit="litres", preparation_time="20")

#     def test_beer_creation(self):
#         self.beer.save()
#         self.assertIsNotNone(self.beer.id)