from django.db import models

# Create your models here.

class Beer(models.Model):
    name = models.CharField(max_length=120)
    tagline = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True, verbose_name="created at", blank=True)
    updated_date = models.DateField(auto_now=True, verbose_name='last updated', blank=True)
    description = models.TextField(default="", blank=True)
    abv = models.IntegerField(blank=True)
    ibu = models.IntegerField(blank=True)
    ebc = models.IntegerField(blank=True)
    ph = models.IntegerField(blank=True)
    attenuation_level = models.FloatField(blank=True)

    def __str__(self):
        return f"{self.name}"

class Volume(models.Model):
    value = models.IntegerField
    unit = models.IntegerField(1, 'litres')
    beer = models.ForeignKey("Beer", on_delete=models.CASCADE, blank=True, related_name="images")

    def __str__(self):
        return f"{self.get_volume_display()}"


class BoilVolume(models.Model):
    value = models.IntegerField
    unit = models.IntegerField(1, 'litres')
    beer = models.ForeignKey("Beer", on_delete=models.CASCADE, blank=True, related_name="images")

    def __str__(self):
        return f"{self.get_boilvolume_display()}"



class BeerImage(models.Model):
    image = models.ImageField(upload_to="product_images")
    beer = models.ForeignKey("Beer", on_delete=models.CASCADE, blank=True, related_name="images")

    def __str__(self):
        return f"{self.image}"



class Method(models.Model):
    mash_temp = models.ForeignKey("MashTemp", on_delete=models.PROTECT)
    fermentation = models.ForeignKey("Fermentation", on_delete=models.PROTECT)


class MashTemp(models.Model):
    value = models.IntegerField
    unit = models.IntegerField(1, 'litres')
    beerproject = models.ForeignKey("Beer", on_delete=models.CASCADE, blank=True, related_name="images")

    def __str__(self):
        return f"{self.get_mashtemp_display()}"


class Fermentation(models.Model):
    value = models.IntegerField
    unit = models.IntegerField(1, 'litres')
    beerproject = models.ForeignKey("Beer", on_delete=models.CASCADE, blank=True, related_name="images")

    def __str__(self):
        return f"{self.get_fermentation_display()}"


class Ingredients(models.Model):
    name = models.CharField(max_length=120)
    type = models.IntegerField((1, 'malt'), (2, "hops"), (3, "yeast"), (4, "other"))
    description = models.TextField(default="", blank=True)
    value = models.IntegerField
    unit = models.IntegerField((1, 'litres'), (2, "kilograms"), (3, "grams"))


class BeerProject(models.Model):
    beer = models.ForeignKey("Beer", on_delete=models.PROTECT, verbose_name="Wybierz piwo")
    volume = models.ForeignKey("Volume", on_delete=models.CASCADE)
    boil_volume = models.ForeignKey("BoilVolume", on_delete=models.CASCADE)
    beer_image = models.ForeignKey("BeerImage", on_delete=models.PROTECT, verbose_name="Wybierz grafikę")
    method = models.ForeignKey("Method", on_delete=models.PROTECT, verbose_name="Wybierz metodę zacierania")
    ingredients = models.ForeignKey("Ingredients", on_delete=models.PROTECT, verbose_name="Składniki")