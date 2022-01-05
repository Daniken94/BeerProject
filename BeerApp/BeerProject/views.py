from django.shortcuts import render
from django.views import View
from .models import BeerProject, Beer, Ingredients, BoilVolume, Method, MashTemp, Fermentation, BeerImage
from .forms import BeerImageForm, AddBeerForm


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

        ingredients_malt = Ingredients.objects.filter(beer_id=id, type=1).order_by('sequence')
        ingredients_hop = Ingredients.objects.filter(beer_id=id, type=2).order_by('sequence')
        ingredients_yeast = Ingredients.objects.filter(beer_id=id, type=3).order_by('sequence')
        ingredients_other = Ingredients.objects.filter(beer_id=id, type=4).order_by('sequence')

        boil_volume = BoilVolume.objects.filter(beer_id=id)
        method = Method.objects.all()
        mash_temp = MashTemp.objects.filter(beer_id=id)
        fermentation = Fermentation.objects.filter(beer_id=id)
        image = BeerImage.objects.get(beer_id=id)
        print(image)
        return render(request, "one_project.html",
                      {'beer': beer, 'project': project, 'ing_malt': ingredients_malt, 'ing_hop': ingredients_hop,
                       'ing_yeast': ingredients_yeast, 'ing_other': ingredients_other, "boil": boil_volume,
                       'method': method, "fermentation": fermentation, "mash_temp": mash_temp, 'image': image})




def beer_add_view(request):
    form = AddBeerForm()

    if request.method == 'POST':
        form = AddBeerForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "add_new_project.html", {'form': form})


# def beer_add_view(request):
#     if request.method == 'POST':
#         form = AddBeerForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     form = AddBeerForm()
#     return render(request, "add_new_project.html", {'form': form})