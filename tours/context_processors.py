from random import sample

from tours.data import title, subtitle, description, departures, tours


def base_information(request):
    random_tours = {}
    tours_keys = sample(tours.keys(), 6)
    for key in tours_keys:
        random_tours[key] = tours[key]

    information = {
        "title": title,
        "subtitle": subtitle,
        "description": description,
        "departures": departures,
        "tours": random_tours,
    }

    return information
