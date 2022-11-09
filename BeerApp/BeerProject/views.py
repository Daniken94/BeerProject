from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views import View
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Beer, Ingredients, BoilVolume, MashTemp, Fermentation, BeerImage
from .forms import AddBeerImageForm, AddBeerForm, AddBeerIngredientsForm, AddBeerMashTempForm, AddBeerFermentationForm, \
    AddBeerBoilVolumeForm


# gunicorn
# VPS server


def View404(request):
    return render(request, "404.html")


class BeerProjectListView(View):
    def get(self, request):
        current_user = request.user.id
        beer = Beer.objects.filter(user_id=current_user).order_by('-brew')
        # image = BeerImage.objects.all()

        return render(request, "project_list.html", {'beer': beer})


class BeerProjectView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['pk']

        # beer = Beer.objects.filter(user=request.user).get(pk=id)
        beer = get_object_or_404(Beer, user=request.user, pk=id)

        ingredients_malt = Ingredients.objects.filter(beer_id=id, type=1).order_by('sequence')
        ingredients_hop = Ingredients.objects.filter(beer_id=id, type=2).order_by('sequence')
        ingredients_yeast = Ingredients.objects.filter(beer_id=id, type=3).order_by('sequence')
        ingredients_other = Ingredients.objects.filter(beer_id=id, type=4).order_by('sequence')

        boil_volume = BoilVolume.objects.filter(beer_id=id)
        mash_temp = MashTemp.objects.filter(beer_id=id)
        fermentation = Fermentation.objects.filter(beer_id=id)
        image = BeerImage.objects.filter(beer_id=id)
        beer_image = Beer.objects.filter(id=id)

        return render(request, "one_project.html",
                      {'beer': beer, 'ing_malt': ingredients_malt, 'ing_hop': ingredients_hop,
                       'ing_yeast': ingredients_yeast, 'ing_other': ingredients_other, "boil": boil_volume,
                       "fermentation": fermentation, "mash_temp": mash_temp, 'image': image, "beer_image": beer_image})

class ProjectAddView(View):
    def get(self, request):
        beer = Beer.objects.all()
        return render(request, "dashboard_project.html", {'beer': beer})


class BeerAddView(View):
    def get(self, request):
        form = AddBeerForm()
        return render(request, "add_new_beer.html", {'form': form})

    def post(self, request):
        form = AddBeerForm(request.POST, request.FILES)
        if form.is_valid():
            beer_user = form.save(commit=False)
            beer_user.user = request.user
            beer_user.save()
        return render(request, "dashboard_project.html", {'form': form})


class BeerImageAddView(View):
    def get(self, request, *args, **kwargs):
        form = AddBeerImageForm(user=request.user)
        return render(request, 'add_new_beer_image.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AddBeerImageForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            beer = form.save(commit=False)
            beer.user = request.user
            beer.save()
        return render(request, 'dashboard_project.html', {'form': form, 'img_obj': beer})


class IngredientsAddView(View):
    def get(self, request, *args, **kwargs):
        form = AddBeerIngredientsForm(user=request.user)
        return render(request, "add_new_ingredients.html", {'form': form})

    def post(self, request, *args, **kwargs):
        form = AddBeerIngredientsForm(request.POST, user=request.user)
        if form.is_valid():
            beer = form.save(commit=False)
            beer.user = request.user
            beer.save()
        return render(request, "dashboard_project.html", {'form': form})


class BoilVolumeAddView(View):
    def get(self, request):
        form = AddBeerBoilVolumeForm(user=request.user)
        return render(request, "add_new_beer_boil_volume.html", {'form': form})

    def post(self, request):
        form = AddBeerBoilVolumeForm(request.POST, user=request.user)
        if form.is_valid():
            beer = form.save(commit=False)
            beer.user = request.user
            beer.save()
        return render(request, "dashboard_project.html", {'form': form})


class MashTempAddView(View):
    def get(self, request):
        form = AddBeerMashTempForm(user=request.user)
        return render(request, "add_new_beer_mashtemp.html", {'form': form})

    def post(self, request):
        form = AddBeerMashTempForm(request.POST, user=request.user)

        if request.method == 'POST':
            form = AddBeerMashTempForm(request.POST, user=request.user)
            if form.is_valid():
                beer = form.save(commit=False)
                beer.user = request.user
                beer.save()
        return render(request, "dashboard_project.html", {'form': form})


class FermentationAddView(View):
    def get(self, request):
        form = AddBeerFermentationForm(user=request.user)
        return render(request, "add_new_beer_fermentation.html", {'form': form})

    def post(self, request):
        form = AddBeerFermentationForm(request.POST, user=request.user)

        if request.method == 'POST':
            form = AddBeerFermentationForm(request.POST, user=request.user)
            if form.is_valid():
                beer = form.save(commit=False)
                beer.user = request.user
                beer.save()
        return render(request, "dashboard_project.html", {'form': form})


class UpdateBeerView(View):
    def get(self, request, pk):
        beer = Beer.objects.get(id=pk)
        form = AddBeerForm(instance=beer)
        return render(request, "add_new_beer.html", {'form': form})

    def post(self, request, pk):
        beer = Beer.objects.get(id=pk)
        form = AddBeerForm(request.POST, request.FILES, instance=beer)
        if form.is_valid():
            form.save()
            return redirect("beerproject:project_list")


class DeleteBeerView(View):
    def get(self, request, pk):
        beer = Beer.objects.get(id=pk)
        return render(request, "delete_beer.html", {"beer": beer})
    def post(self, request, pk):
        beer = Beer.objects.get(id=pk)
        beer.delete()
        return redirect("beerproject:project_list")


class UpdateImageView(View):
    def get(self, request, pk):
        image = BeerImage.objects.get(id=pk)
        form = AddBeerImageForm(user=request.user, instance=image)
        return render(request, "add_new_beer_image.html", {'form': form, "image": image})

    def post(self, request, pk):
        image = BeerImage.objects.get(id=pk)
        form = AddBeerImageForm(request.POST, request.FILES, user=request.user, instance=image)
        if form.is_valid():
            beer = form.save(commit=False)
            beer.user = request.user
            beer.save()
            return redirect("beerproject:project_list")


class DeleteImageView(View):
    def get(self, request, pk):
        image = BeerImage.objects.get(id=pk)
        return render(request, "delete_image.html", {"item": image})

    def post(self, request, pk):
        image = BeerImage.objects.get(id=pk)
        image.delete()
        return redirect("beerproject:project_list")



class UpdateIngredientsView(View):
    def get(self, request, pk):
        ingredient = Ingredients.objects.get(id=pk)
        # beer_id = Ingredients.objects.filter(beer_id=id)
        form = AddBeerIngredientsForm(user=request.user, instance=ingredient)
        return render(request, "add_new_ingredients.html", {'form': form})

    def post(self, request, pk):
        ingredient = Ingredients.objects.get(id=pk)
        form = AddBeerIngredientsForm(request.POST, user=request.user, instance=ingredient)
        if form.is_valid():
            beer = form.save(commit=False)
            beer.user = request.user
            beer.save()
            # ingredient = form.save()
            return redirect(f"beerproject:project_list")  # +f"#ingredient_{ingredient.id}"


class DeleteIngredientsView(View):
    def get(self, request, pk):
        ingredient = Ingredients.objects.get(id=pk)
        return render(request, "delete_item.html", {"item": ingredient})
    def post(self, request, pk):
        ingredient = Ingredients.objects.get(id=pk)
        ingredient.delete()
        return redirect("beerproject:project_list")


class UpdateMashtempView(View):
    def get(self, request, pk):
        mashtemp = MashTemp.objects.get(id=pk)
        form = AddBeerMashTempForm(user=request.user, instance=mashtemp)
        return render(request, "add_new_beer_mashtemp.html", {'form': form})

    def post(self, request, pk):
        mashtemp = MashTemp.objects.get(id=pk)
        form = AddBeerMashTempForm(request.POST, user=request.user, instance=mashtemp)
        if form.is_valid():
            beer = form.save(commit=False)
            beer.user = request.user
            beer.save()
            return redirect("beerproject:project_list")


class DeleteMashtempView(View):
    def get(self, request, pk):
        mashtemp = MashTemp.objects.get(id=pk)
        return render(request, "delete_mashtemp.html", {"item": mashtemp})

    def post(self, request, pk):
        mashtemp = MashTemp.objects.get(id=pk)
        mashtemp.delete()
        return redirect("beerproject:project_list")


class UpdateFermentationView(View):
    def get(self, request, pk):
        fermentation = Fermentation.objects.get(id=pk)
        form = AddBeerFermentationForm(user=request.user, instance=fermentation)
        return render(request, "add_new_beer_fermentation.html", {'form': form})

    def post(self, request, pk):
        fermentation = Fermentation.objects.get(id=pk)
        form = AddBeerFermentationForm(request.POST, user=request.user, instance=fermentation)
        if form.is_valid():
            beer = form.save(commit=False)
            beer.user = request.user
            beer.save()
            return redirect("beerproject:project_list")


class DeleteFermentationView(View):
    def get(self, request, pk):
        fermentation = Fermentation.objects.get(id=pk)
        return render(request, "delete_fermentation.html", {"item": fermentation})

    def post(self, request, pk):
        fermentation = Fermentation.objects.get(id=pk)
        fermentation.delete()
        return redirect("beerproject:project_list")


class UpdateBoilView(View):
    def get(self, request, pk):
        boil = BoilVolume.objects.get(id=pk)
        form = AddBeerBoilVolumeForm(user=request.user, instance=boil)
        return render(request, "add_new_beer_boil_volume.html", {'form': form})

    def post(self, request, pk):
        boil = BoilVolume.objects.get(id=pk)
        form = AddBeerBoilVolumeForm(request.POST, user=request.user, instance=boil)
        if form.is_valid():
            beer = form.save(commit=False)
            beer.user = request.user
            beer.save()
            return redirect("beerproject:project_list")


class DeleteBoilView(View):
    def get(self, request, pk):
        boil = BoilVolume.objects.get(id=pk)
        return render(request, "delete_boil.html", {"item": boil})

    def post(self, request, pk):
        boil = BoilVolume.objects.get(id=pk)
        boil.delete()
        return redirect("beerproject:project_list")




