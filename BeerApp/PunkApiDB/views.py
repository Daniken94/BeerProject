from urllib import request

from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import requests


# superuser - kamil
# email - kamil@gmail.com
# hasło - kamil

def homepage(request):
    return render(request, "homepage.html")


def list_of_beers_type(request):
    url = 'https://api.punkapi.com/v2/beers?per_page=80'
    response = requests.get(url).json()
    return render(request, "list_of_beers_type.html", {"response": response})


def list_of_beers_type_page2(request):
    url = 'https://api.punkapi.com/v2/beers?page=2&per_page=80'
    response = requests.get(url).json()
    return render(request, "list_of_beers_type_page2.html", {"response": response})


def list_of_beers_type_page3(request):
    url = 'https://api.punkapi.com/v2/beers?page=3&per_page=80'
    response = requests.get(url).json()
    return render(request, "list_of_beers_type_page3.html", {"response": response})


def list_of_beers_type_page4(request):
    url = 'https://api.punkapi.com/v2/beers?page=4&per_page=80'
    response = requests.get(url).json()
    return render(request, "list_of_beers_type_page4.html", {"response": response})


def list_of_beers_type_page5(request):
    url = 'https://api.punkapi.com/v2/beers?page=5&per_page=80'
    response = requests.get(url).json()
    return render(request, "list_of_beers_type_page5.html", {"response": response})


class list_of_beers(View):
    def get(self, request):
        url = 'https://api.punkapi.com/v2/beers?per_page=80'
        response = requests.get(url).json()
        return render(request, "list_of_beers.html", {"response": response})
    def post(self):
        pass



def list_of_beers_page2(request):
    url = 'https://api.punkapi.com/v2/beers?page=2&per_page=80'
    response = requests.get(url).json()
    return render(request, "list_of_beers_page2.html", {"response": response})


def list_of_beers_page3(request):
    url = 'https://api.punkapi.com/v2/beers?page=3&per_page=80'
    response = requests.get(url).json()
    return render(request, "list_of_beers_page3.html", {"response": response})


def list_of_beers_page4(request):
    url = 'https://api.punkapi.com/v2/beers?page=4&per_page=80'
    response = requests.get(url).json()
    return render(request, "list_of_beers_page4.html", {"response": response})


def list_of_beers_page5(request):
    url = 'https://api.punkapi.com/v2/beers?page=5&per_page=80'
    response = requests.get(url).json()
    return render(request, "list_of_beers_page5.html", {"response": response})


class OneBeerView(View):
    def get(self, request):
        beer_name = 'Buzz'
        url = f"https://api.punkapi.com/v2/beers?beer_name={beer_name}"
        response = requests.get(url).json()

        return render(request, "one_beer.html", {"response": response})

    def post(self, request):
        pass


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
