from django.shortcuts import render
from django_tables2 import RequestConfig

from neo_tracker.helpers.neo_table import NeoTable
from neo_tracker.services import near_earth_object_fetcher_service


def index(request):
    table = NeoTable(near_earth_object_fetcher_service.get_objects())
    RequestConfig(request).configure(table)
    return render(request, 'neo_tracker/index.html', context={
        'table': table
    })
