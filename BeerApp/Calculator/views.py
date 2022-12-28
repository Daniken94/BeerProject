from django.shortcuts import render
from django.views import View
from decimal import Decimal
from .forms import AlcCalcForm, AutCalcForm, IBUCalcForm, WaterCalcForm



class AlcCalcView(View):
    def get(self, request):
        form = AlcCalcForm()
        return render(request, "alc_calc.html", {'form': form})

    def post(self, request):
        form = AlcCalcForm(request.POST)
        if form.is_valid():
            OG = form.cleaned_data["OG"]
            FG = form.cleaned_data["FG"]
            alc_prime = round(((OG - FG) / 1.938), 1)
            attenuation = round((100 - (FG * 100 / OG)), 1)
            alc = f"The alcohol level in your beer is {alc_prime} %"
            aut = f"The auttenuation level is {attenuation} %"
            return render(request, "alc_calc.html", {'form': form, "alc": alc, "aut": aut})
        return render(request, "alc_calc.html", {'form': form})



class AutCalcView(View):
    def get(self, request):
        form = AutCalcForm()
        return render(request, "brewhouse_performance.html", {'form': form})

    def post(self, request):
        form = AutCalcForm(request.POST)
        if form.is_valid():
            value_beer = form.cleaned_data["value_beer"]
            blg = form.cleaned_data["blg"]
            value_malt = form.cleaned_data["value_malt"]
            aut_prime = round((((value_beer * blg) * 1.05) / value_malt), 2)
            aut = f"The performance level of your brewhouse is {aut_prime}%"
            return render(request, "brewhouse_performance.html", {'form': form, "aut": aut})
        return render(request, "brewhouse_performance.html", {'form': form})



class IBUCalcView(View):
    def get(self, request):
        form = IBUCalcForm()
        return render(request, "ibu_calc.html", {'form': form})

    def post(self, request):
        form = IBUCalcForm(request.POST)
        if form.is_valid():
            hops = form.cleaned_data["hops"]
            acids = form.cleaned_data["acids"]
            utilization = form.cleaned_data["utilization"]
            value_beer = form.cleaned_data["value_beer"]
            ibu1 = (hops * acids * utilization)
            ibu2 = value_beer * 20
            ibu_prime = int(ibu1 / ibu2)
            ibu = f"The IBU level in your beer is {ibu_prime}"
            return render(request, "ibu_calc.html", {'form': form, "ibu": ibu})
        return render(request, "ibu_calc.html", {'form': form})



class EBCCalcView(View):
    def get(self, request):
        return render(request, "ebc_calc.html")



class WaterCalcView(View):
    def get(self, request):
        form = WaterCalcForm()
        return render(request, "water_calc.html", {'form': form})

    def post(self, request):
        form = WaterCalcForm(request.POST)
        if form.is_valid():
            malt = form.cleaned_data["malt"]
            water = 3.5 * float(malt)
            result = f"You need {water} litres of water for this malt."
            return render(request, "water_calc.html", {'form': form, "result": result})
        return render(request, "water_calc.html", {'form': form})
