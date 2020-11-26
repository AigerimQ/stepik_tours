from random import sample

from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View

from tours.data import tours


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, данная страница не найдена((')


def custom_handler500(request):
    return HttpResponseServerError('Ой, что-то стряслось с сервером... Скоро все починим')


class MainView(View):

    def get(self, request):
        random_tours = {}
        number_of_tours_on_page = 6
        tours_keys = sample(tours.keys(), number_of_tours_on_page)
        for key in tours_keys:
            random_tours[key] = tours[key]
        max_stars = "★★★★★"

        context = {
            "tours": random_tours,
            "stars": max_stars
        }

        return render(request, 'index.html', context=context)
