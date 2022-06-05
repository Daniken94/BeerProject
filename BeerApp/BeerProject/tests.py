from django.test import TestCase
from .models import Beer, Ingredients, BoilVolume, MashTemp, Fermentation, BeerImage
from django.contrib.auth.models import User
import tempfile
import mock
from django.core.files import File


class BeerModelTestCase(TestCase):
    def setUp(self):    #uruchomiona metoda przy każdym rozpoczęciu testów
        self.user = User.objects.create(username="Kamil")
        self.beer = Beer(name="Atak Chmielu", tagline="IPA", beer_volume="20", unit="litres", 
                            preparation_time="20", user = self.user)
        

    def test_beer_creation(self):
        self.beer.save()
        self.assertIsNotNone(self.beer.id)


    def test_boil_volume_creation(self):
        self.beer.save()
        self.boil = BoilVolume(value="20", unit="litres", substance="water", beer=self.beer)
        self.boil.save()
        self.assertIsNotNone(self.boil.id)


    # def test_beer_image_creation(self):
    #     self.beer.save()
    #     file_mock = mock.MagicMock(spec=File, name='FileMock')
    #     self.image = BeerImage(image=file_mock)
    #     self.image.save()


    def test_mash_temp_creation(self):
        self.beer.save()
        self.mash = MashTemp(value_temperature="20", unit="celsius", duration="30", 
                                sequence="1", beer=self.beer)
        self.mash.save()
        self.assertIsNotNone(self.mash.id)


    def test_fermentation_creation(self):
        self.beer.save()
        self.fermentation = Fermentation(value_temperature="20", unit="celsius", duration="30", 
                                            sequence="1", beer=self.beer)
        self.fermentation.save()
        self.assertIsNotNone(self.fermentation.id)


    def test_ingredients_creation(self):
        self.beer.save()
        self.ingredients = Ingredients(name="Marynka", type="2", description="testowy opis", 
                                        value="30", unit="grams", sequence="1", sequence_unit="30 minuta", 
                                        beer=self.beer)
        self.ingredients.save()
        self.assertIsNotNone(self.ingredients.id)
    