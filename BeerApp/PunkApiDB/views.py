from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import requests


# superuser - kamil
# email - kamil@gmail.com
# hasło - kamil


def list_of_beers_type(request):
    url = 'https://api.punkapi.com/v2/beers?per_page=80'
    response = requests.get(url).json()
    return render(request, "list_of_beers_type.html", {"response": response})


def one_beer(request):
    id = 1

    url = f"https://api.punkapi.com/v2/beers/{id}"

    response = requests.get(url).json()

    beer_info = {
        'name': response[0],
        'tagline': response[0],
    }

    print(beer_info)

    return render(request, "list_of_beers_type.html", {"response": response})
