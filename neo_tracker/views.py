from django.shortcuts import render

from neo_tracker.helpers.neo_table import NeoTable
from neo_tracker.services import near_earth_object_fetcher_service


def index(request):
    table = NeoTable(near_earth_object_fetcher_service.get_objects())

    return render(request, 'neo_tracker/index.html', context={
        'table': table
    })
