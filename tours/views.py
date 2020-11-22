from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.views import View

from tours.data import departures, tours


class DepartureView(View):
    def get(self, request, departure):
        if departure not in departures:
            return HttpResponseNotFound('Ой, данная страница не найдена((')
        else:
            departure_tours = {}
            tours_price = []
            tours_nights = []
            for tour_id, tour in tours.items():
                if departure in tour.values():
                    departure_tours[tour_id] = tours[tour_id]
                    tours_price.append(tour["price"])
                    tours_nights.append(tour["nights"])

            context = {
                "departure": departures[departure],
                "tours": departure_tours,
                "min_price": min(tours_price),
                "max_price": max(tours_price),
                "min_nights": min(tours_nights),
                "max_nights": max(tours_nights),
            }

            return render(request, 'departure.html', context=context)


class TourView(View):
    def get(self, request, id):
        if id not in tours:
            return HttpResponseNotFound('Ой, данная страница не найдена((')
        else:
            context = {
                "tour": tours[id],
                "departure": departures[str(tours[id]["departure"])],
            }

            return render(request, 'tour.html', context=context)
