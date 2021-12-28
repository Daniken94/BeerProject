from django.shortcuts import render
import requests


def home(request):
    response = requests.get("https://api.punkapi.com/v2/beers").json
    return render(request, "list_of_beers_type.html", {"response": response})
