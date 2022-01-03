from django.db import models


# Create your models here.

class Beer(models.Model):
    BEER_CHOICES = (
        (1, 'litres'),
    )

    name = models.CharField(max_length=120)
    tagline = models.CharField(max_length=120, verbose_name="Beer style")
    description = models.TextField(default="", blank=True, null=True)
    abv = models.FloatField(blank=True, null=True)
    ibu = models.IntegerField(blank=True, null=True)
    ebc = models.IntegerField(blank=True, null=True)
    ph = models.IntegerField(blank=True, null=True)
    attenuation_level = models.FloatField(blank=True, null=True)
    beer_value = models.IntegerField()
    unit = models.IntegerField(choices=BEER_CHOICES)

    def __str__(self):
        return f"{self.name}"

    # usunąc null=True w textfield

class BoilVolume(models.Model):
    boil_choices = (
        (1, 'litres'),
    )
    value = models.IntegerField()
    unit = models.IntegerField(choices=boil_choices)
    substance = models.CharField(max_length=120)
    beer = models.ForeignKey("Beer", on_delete=models.CASCADE, blank=True)

    # usunąć beer

    def __str__(self):
        return f"{self.value} {self.get_unit_display()} of {self.substance}"


class BeerImage(models.Model):
    image = models.ImageField(upload_to="product_images")

    def __str__(self):
        return f"{self.image}"


class Method(models.Model):
    mash_temp = models.ManyToManyField("MashTemp")
    fermentation = models.ManyToManyField("Fermentation")

    # multiple choices

class MashTemp(models.Model):
    mashtemp_choices = (
        (1, 'celsius'),
    )

    value_temperature = models.IntegerField()
    unit = models.IntegerField(choices=mashtemp_choices)
    duration = models.IntegerField(help_text="How long in minutes")

    def __str__(self):
        return f"{self.value_temperature} {self.get_unit_display()} {self.duration} minutes"

    # celsius FOR 60 minutes
    # kolejność

class Fermentation(models.Model):
    fermentation_choices = (
        (1, 'celsius'),
    )

    value_temperature = models.IntegerField()
    unit = models.IntegerField(choices=fermentation_choices)
    duration = models.IntegerField(help_text="How long in days", blank=True, null=True)

    def __str__(self):
        return f"{self.value_temperature} {self.get_unit_display()} {self.duration} days"

    # kolejność

class Ingredients(models.Model):
    type_choices = (
        (1, 'malt'),
        (2, "hops"),
        (3, "yeast"),
        (4, "other"),
    )

    unit_choices = (
        (1, 'litres'),
        (2, "kilograms"),
        (3, "grams"),
    )

    purpose_choices = (
        (1, 'bittering'),
        (2, "aroma"),
        (3, "dual use"),
        (4, "malt")
    )


    name = models.CharField(max_length=120)
    type = models.IntegerField(choices=type_choices)
    description = models.TextField(default="", blank=True, null=True)
    value = models.FloatField()
    unit = models.IntegerField(choices=unit_choices)
    ebc = models.IntegerField(blank=True, null=True)
    purpose = models.IntegerField(choices=purpose_choices, blank=True, null=True)
    aac = models.IntegerField(blank=True, verbose_name="Alfa acid", null=True)
    country = models.CharField(max_length=120, blank=True, null=True)

    # description null true usunąć, country usunąc null

    class Meta:
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return f"{self.name} {self.get_type_display()} {self.get_unit_display()} {self.get_purpose_display()}"


class BeerProject(models.Model):
    beer = models.ForeignKey("Beer", on_delete=models.PROTECT, verbose_name="Choose beer")
    boil_volume = models.ForeignKey("BoilVolume", on_delete=models.PROTECT)
    method = models.ForeignKey("Method", on_delete=models.PROTECT, verbose_name="Choose mash method")
    ingredients = models.ManyToManyField("Ingredients", verbose_name="Ingredients")
    beer_image = models.ForeignKey("BeerImage", on_delete=models.PROTECT, verbose_name="Choose image")
    created_date = models.DateField(auto_now_add=True, verbose_name="created at", blank=True)
    updated_date = models.DateField(auto_now=True, verbose_name='last updated', blank=True)

    def __str__(self):
        return f"{self.beer}"
