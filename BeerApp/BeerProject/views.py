from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import DeleteView
from django.urls import reverse
from .models import Beer, Ingredients, BoilVolume, MashTemp, Fermentation, BeerImage
from .forms import AddBeerImageForm, AddBeerForm, AddBeerIngredientsForm, AddBeerMashTempForm, AddBeerFermentationForm, AddBeerBoilVolumeForm


class BeerProjectListView(View):
    def get(self, request):
        beer = Beer.objects.all().order_by('id')

        return render(request, "project_list.html", {'beer': beer})


class BeerProjectView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['pk']

        beer = Beer.objects.get(pk=id)

        ingredients_malt = Ingredients.objects.filter(beer_id=id, type=1).order_by('sequence')
        ingredients_hop = Ingredients.objects.filter(beer_id=id, type=2).order_by('sequence')
        ingredients_yeast = Ingredients.objects.filter(beer_id=id, type=3).order_by('sequence')
        ingredients_other = Ingredients.objects.filter(beer_id=id, type=4).order_by('sequence')

        boil_volume = BoilVolume.objects.filter(beer_id=id)
        mash_temp = MashTemp.objects.filter(beer_id=id)
        fermentation = Fermentation.objects.filter(beer_id=id)
        image = BeerImage.objects.get(beer_id=id)

        return render(request, "one_project.html",
                      {'beer': beer, 'ing_malt': ingredients_malt, 'ing_hop': ingredients_hop,
                       'ing_yeast': ingredients_yeast, 'ing_other': ingredients_other, "boil": boil_volume,
                       "fermentation": fermentation, "mash_temp": mash_temp, 'image': image})



def project_add_view(request):
    beer = Beer.objects.all()
    return render(request, "dashboard_project.html", {'beer': beer})


class BeerAddView(View):
    def get(self, request):
        form = AddBeerForm()
        return render(request, "add_new_beer.html", {'form': form})

    def post(self, request):
        form = AddBeerForm()

        if request.method == 'POST':
            form = AddBeerForm(request.POST)
            if form.is_valid():
                form.save()
        return render(request, "dashboard_project.html", {'form': form})


def beer_image_add_view(request):
    if request.method == 'POST':
        form = AddBeerImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'dashboard_project.html', {'form': form, 'img_obj': img_obj})
    else:
        form = AddBeerImageForm()
    return render(request, 'add_new_beer_image.html', {'form': form})


class IngredientsAddView(View):
    def get(self, request):
        form = AddBeerIngredientsForm()
        return render(request, "add_new_ingredients.html", {'form': form})

    def post(self, request):
        form = AddBeerIngredientsForm()

        if request.method == 'POST':
            form = AddBeerIngredientsForm(request.POST)
            if form.is_valid():
                form.save()
        return render(request, "dashboard_project.html", {'form': form})


class BoilVolumeAddView(View):
    def get(self, request):
        form = AddBeerBoilVolumeForm()
        return render(request, "add_new_beer_boil_volume.html", {'form': form})

    def post(self, request):
        form = AddBeerBoilVolumeForm()

        if request.method == 'POST':
            form = AddBeerBoilVolumeForm(request.POST)
            if form.is_valid():
                form.save()
        return render(request, "dashboard_project.html", {'form': form})


class MashTempAddView(View):
    def get(self, request):
        form = AddBeerMashTempForm()
        return render(request, "add_new_beer_mashtemp.html", {'form': form})

    def post(self, request):
        form = AddBeerMashTempForm()

        if request.method == 'POST':
            form = AddBeerMashTempForm(request.POST)
            if form.is_valid():
                form.save()
        return render(request, "dashboard_project.html", {'form': form})


class FermentationAddView(View):
    def get(self, request):
        form = AddBeerFermentationForm()
        return render(request, "add_new_beer_fermentation.html", {'form': form})

    def post(self, request):
        form = AddBeerFermentationForm()

        if request.method == 'POST':
            form = AddBeerFermentationForm(request.POST)
            if form.is_valid():
                form.save()
        return render(request, "dashboard_project.html", {'form': form})


def update_beer_view(request, pk):
    beer = Beer.objects.get(id=pk)
    form = AddBeerForm(instance=beer)

    if request.method == 'POST':
        form = AddBeerForm(request.POST, instance=beer)
        if form.is_valid():
            form.save()
            return redirect("beerproject:project_list")
    return render(request, "add_new_beer.html", {'form': form})


def delete_beer_view(request, pk):
    beer = Beer.objects.get(id=pk)
    if request.method == "POST":
        beer.delete()
        return redirect("beerproject:project_list")
    return render(request, "delete_beer.html", {"beer": beer})


def update_ingredients_view(request, pk):
    ingredient = Ingredients.objects.get(id=pk)
    form = AddBeerIngredientsForm(instance=ingredient)

    if request.method == 'POST':
        form = AddBeerIngredientsForm(request.POST, instance=ingredient)
        if form.is_valid():
                                                                   #ingredient = form.save()
            return redirect("beerproject:project_list")            #+f"#ingredient_{ingredient.id}")
    return render(request, "add_new_ingredients.html", {'form': form})


def delete_ingredients_view(request, pk):
    ingredient = Ingredients.objects.get(id=pk)
    if request.method == "POST":
        ingredient.delete()
        return redirect("beerproject:project_list")
    return render(request, "delete_item.html", {"item": ingredient})


def update_mashtemp_view(request, pk):
    mashtemp = MashTemp.objects.get(id=pk)
    form = AddBeerMashTempForm(instance=mashtemp)

    if request.method == 'POST':
        form = AddBeerMashTempForm(request.POST, instance=mashtemp)
        if form.is_valid():
            form.save()
            return redirect("beerproject:project_list")
    return render(request, "add_new_beer_mashtemp.html", {'form': form})


def delete_mashtemp_view(request, pk):
    mashtemp = MashTemp.objects.get(id=pk)
    if request.method == "POST":
        mashtemp.delete()
        return redirect("beerproject:project_list")
    return render(request, "delete_mashtemp.html", {"item": mashtemp})


def update_fermentation_view(request, pk):
    fermentation = Fermentation.objects.get(id=pk)
    form = AddBeerFermentationForm(instance=fermentation)

    if request.method == 'POST':
        form = AddBeerFermentationForm(request.POST, instance=fermentation)
        if form.is_valid():
            form.save()
            return redirect("beerproject:project_list")
    return render(request, "add_new_beer_fermentation.html", {'form': form})


def delete_fermentation_view(request, pk):
    fermentation = Fermentation.objects.get(id=pk)
    if request.method == "POST":
        fermentation.delete()
        return redirect("beerproject:project_list")
    return render(request, "delete_fermentation.html", {"item": fermentation})


def update_boil_view(request, pk):
    boil = BoilVolume.objects.get(id=pk)
    form = AddBeerBoilVolumeForm(instance=boil)

    if request.method == 'POST':
        form = AddBeerBoilVolumeForm(request.POST, instance=boil)
        if form.is_valid():
            form.save()
            return redirect("beerproject:project_list")
    return render(request, "add_new_beer_boil_volume.html", {'form': form})


def delete_boil_view(request, pk):
    boil = BoilVolume.objects.get(id=pk)
    if request.method == "POST":
        boil.delete()
        return redirect("beerproject:project_list")
    return render(request, "delete_boil.html", {"item": boil})
