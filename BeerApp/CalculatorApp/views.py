from django.shortcuts import render
from django.views import View
from .models import BeerProject, Beer, Ingredients


class BeerProjectListView(View):
    def get(self, request):
        project = BeerProject.objects.all().order_by('id')
        beer = Beer.objects.all().order_by('id')

        return render(request, "project_list.html", {'project': project, 'beer': beer})


class BeerProjectView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['pk']

        beer = Beer.objects.get(pk=id)
        project = BeerProject.objects.get(pk=id)
        ingredients_malt = Ingredients.objects.filter(beer_id=id, type=1)
        ingredients_hop = Ingredients.objects.filter(beer_id=id, type=2)
        ingredients_yeast = Ingredients.objects.filter(beer_id=id, type=3)
        og = Beer.objects.get(pk=id)
        fg = Beer.objects.get(pk=id)
        abv = Beer.objects.get(pk=id)
        return render(request, "one_project.html",
                      {'beer': beer, 'project': project, 'ing_malt': ingredients_malt, 'ing_hop': ingredients_hop,
                       'ing_yeast': ingredients_yeast, "og": og, "fg": fg, "abv": abv})
