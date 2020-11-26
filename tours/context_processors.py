from tours.data import title, subtitle, description, departures


def base_information(request):

    information = {
        "title": title,
        "subtitle": subtitle,
        "description": description,
        "departures": departures,
    }

    return information
