from django.shortcuts import render
from django.views import View
from decimal import Decimal
from .forms import AlcCalcForm, AutCalcForm, IBUCalcForm



class AlcCalcView(View):
    def get(self, request):
        form = AlcCalcForm()
        return render(request, "alc_calc.html", {'form': form})

    def post(self, request):
        form = AlcCalcForm()
        OG = float(request.POST.get("OG"))
        FG = float(request.POST.get("FG"))
        alc_prime = round(((OG-FG) / 1.938), 1)
        alc = f"The alcohol level in your beer is {alc_prime} %"
        if request.method == 'POST':
            form = AlcCalcForm(request.POST)
            if form.is_valid():
                return render(request, "alc_calc.html", {'form': form, "alc": alc})
        return render(request, "alc_calc.html", {'form': form})



class AutCalcView(View):
    def get(self, request):
        form = AutCalcForm()
        return render(request, "attenuation_level.html", {'form': form})

    def post(self, request):
        form = AutCalcForm()
        value_beer = float(request.POST.get("value_beer"))
        blg = float(request.POST.get("blg"))
        value_malt = float(request.POST.get("value_malt"))
        aut_prime = round((((value_beer * blg) * 1.05) / value_malt), 2)
        aut = f"The attenuation level in your beer is {aut_prime}%"
        if request.method == 'POST':
            form = AutCalcForm(request.POST)
            if form.is_valid():
                return render(request, "attenuation_level.html", {'form': form, "aut": aut})
        return render(request, "attenuation_level.html", {'form': form})




class IBUCalcView(View):
    def get(self, request):
        form = IBUCalcForm()
        return render(request, "ibu_calc.html", {'form': form})

    def post(self, request):
        form = IBUCalcForm()
        hops = float(request.POST.get("hops"))
        acids = float(request.POST.get("acids"))
        utilization = float(request.POST.get("utilization"))
        value_beer = float(request.POST.get("value_beer"))
        ibu1 = (hops * acids * utilization)
        ibu2 = value_beer * 10
        ibu_prime = round(ibu1 / ibu2, 2)
        ibu = f"The IBU level in your beer is {ibu_prime}"
        if request.method == 'POST':
            form = IBUCalcForm(request.POST)
            if form.is_valid():
                return render(request, "ibu_calc.html", {'form': form, "ibu": ibu})
        return render(request, "ibu_calc.html", {'form': form})



class EBCCalcView(View):
    def get(self, request):
        return render(request, "ebc_calc.html")