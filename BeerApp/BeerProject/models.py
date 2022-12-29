from django.db import models
from django.contrib.auth.models import User


class Beer(models.Model):
    BEER_CHOICES = (
        ('litres', 'litres'),
    )

    brew = models.IntegerField(help_text="Brew number")
    name = models.CharField(max_length=120)
    tagline = models.CharField(max_length=120, verbose_name="Beer style")
    description = models.TextField(default="", blank=True)
    og = models.FloatField(blank=True, null=True, verbose_name="Gęstość początkowa BLG")
    fg = models.FloatField(blank=True, null=True, verbose_name="Gęstość końcowa BLG")
    ibu = models.IntegerField(blank=True, null=True)
    ebc = models.CharField(max_length=120, blank=True, null=True)
    ph = models.IntegerField(blank=True, null=True)
    alc = models.FloatField(blank=True, null=True)
    attenuation_level = models.FloatField(blank=True, null=True)
    beer_volume = models.FloatField()
    unit = models.CharField(max_length=50, choices=BEER_CHOICES, default="litres")
    created_date = models.DateField(auto_now_add=True, verbose_name="created at", blank=True)
    brew_date = models.DateField(verbose_name="brewed at", blank=True, null=True, help_text="np. 01.01.2023")
    updated_date = models.DateField(auto_now=True, verbose_name='last updated', blank=True)
    bootled_date = models.DateField(verbose_name="bootled at", blank=True, null=True, help_text="np. 01.01.2023")
    preparation_time = models.IntegerField(verbose_name="Full time for mash up", blank=True, null=True)
    boiling_time = models.IntegerField(verbose_name="Full time for boiling", blank=True, null=True)
    beer_image = models.ImageField(upload_to="product_images", null=True, default="product_images/default.png")
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if self.og and self.fg is not None:
            self.alc = round(((self.og - self.fg) / 1.938), 1)
            self.attenuation_level = round((100 - (self.fg * 100 / self.og)), 1)
        else:
            self.alc = 0
            self.attenuation_level = 0
        super(Beer, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} by {self.user}"


class BoilVolume(models.Model):
    boil_choices = (
        ('litres', 'litres'),
    )

    value = models.IntegerField()
    unit = models.CharField(max_length=10, choices=boil_choices, default="litres")
    substance = models.CharField(max_length=120, default="Water")
    beer = models.ForeignKey("Beer", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.value} {self.get_unit_display()} of {self.substance}"



class MashTemp(models.Model):
    unit_choices = (
        ("celsius", 'celsius'),
    )

    sequence_choices = (
        (1, 'first'),
        (2, 'second'),
        (3, 'third'),
        (4, 'fourth'),
        (5, 'fifth'),
        (6, 'sixth'),
        (7, 'seventh'),
        (8, 'eighth'),
        (9, 'ninth'),
        (10, 'tenth'),
    )

    value_temperature = models.IntegerField()
    unit = models.CharField(max_length=10, choices=unit_choices, default="celsius")
    duration = models.IntegerField(help_text="How long in minutes")
    sequence = models.IntegerField(choices=sequence_choices)
    beer = models.ForeignKey("Beer", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.value_temperature} {self.get_unit_display()} for {self.duration} minutes"


class Fermentation(models.Model):
    unit_choices = (
        ('celsius', 'celsius'),
    )

    sequence_choices = (
        (1, 'first'),
        (2, 'second'),
        (3, 'third'),
        (4, 'fourth'),
        (5, 'fifth'),
    )

    value_temperature = models.IntegerField()
    unit = models.CharField(max_length=10, choices=unit_choices, default="celsius")
    duration = models.IntegerField(help_text="How long in days", blank=True, null=True)
    sequence = models.IntegerField(choices=sequence_choices)
    beer = models.ForeignKey("Beer", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.value_temperature} {self.get_unit_display()} for {self.duration} days"


class Ingredients(models.Model):
    type_choices = (
        (1, 'malt'),
        (2, "hops"),
        (3, "yeast"),
        (4, "other"),
    )

    unit_choices = (
        ('litres', 'litres'),
        ("kilograms", "kilograms"),
        ("grams", "grams"),
        ("item", "item"),
    )

    purpose_choices = (
        ('bittering', 'bittering'),
        ("aroma", "aroma"),
        ("dual use", "dual use"),
    )

    sequence_choices = (
        (1, 'first'),
        (2, 'second'),
        (3, 'third'),
        (4, 'fourth'),
        (5, 'fifth'),
        (6, 'sixth'),
        (7, 'seventh'),
        (8, 'eighth'),
        (9, 'ninth'),
        (10, 'tenth'),
    )

    name = models.CharField(max_length=120)
    concern = models.CharField(max_length=120, blank=True, null=True)
    type = models.IntegerField(choices=type_choices)
    description = models.TextField(default="", blank=True)
    value = models.FloatField()
    unit = models.CharField(max_length=50, choices=unit_choices)
    ebc = models.CharField(max_length=120, blank=True, null=True)
    purpose = models.CharField(max_length=50, choices=purpose_choices, blank=True, null=True)
    aac = models.FloatField(blank=True, verbose_name="Alfa acid", null=True)
    country = models.CharField(max_length=120, blank=True)
    sequence = models.IntegerField(choices=sequence_choices)
    sequence_unit = models.CharField(default="1", max_length=120, verbose_name="W której minucie dodać składnik")
    beer = models.ForeignKey("Beer", on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return f"{self.name} {self.get_type_display()} {self.get_unit_display()} {self.get_purpose_display()} {self.beer}"
