from django.contrib import admin
from . import models


admin.site.register(models.Beer)
admin.site.register(models.BoilVolume)
admin.site.register(models.BeerImage)
admin.site.register(models.Method)
admin.site.register(models.MashTemp)
admin.site.register(models.Fermentation)
admin.site.register(models.Ingredients)
admin.site.register(models.BeerProject)

