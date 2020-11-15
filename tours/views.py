from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.views import View


class DepartureView(View):
    def get(self, request, departure):
        departures = {
            "msk": "Из Москвы",
            "spb": "Из Петербурга",
            "nsk": "Из Новосибирска",
            "ekb": "Из Екатеринбурга",
            "kazan": "Из Казани"
        }

        if departure not in departures:
            return HttpResponseNotFound('Ой, данная страница не найдена((')
        else:
            context = {
                "departure": departures[departure]
            }

            return render(request, 'departure.html', context=context)


class TourView(View):
    def get(self, request, id):
        tours = {
            1: "Marina Lake Hotel & Spa",
            2: "Baroque Hotel",
            3: "Voyager Resort",
            4: "Orbit Hotel",
            5: "Atlantis Cabin Hotel",
            6: "Light Renaissance Hotel",
            7: "King's Majesty Hotel",
            8: "Crown Hotel",
            9: "Seascape Resort",
            10: "Rose Sanctum Hotel",
            11: "Viridian Obelisk Hotel & Spa",
            12: "Saffron Tundra Hotel & Spa",
            13: "Traveller Resort",
            14: "History Hotel & Spa",
            15: "Riverside Lagoon Hotel & Spa",
            16: "History Hotel & Spa",
        }

        if id not in tours:
            return HttpResponseNotFound('Ой, данная страница не найдена((')
        else:
            context = {
                "tour": tours[id]
            }

            return render(request, 'tour.html', context=context)
