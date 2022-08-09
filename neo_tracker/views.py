from django.contrib import messages
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django_tables2 import RequestConfig
from requests import HTTPError

from neo_tracker.helpers.date_validator import *
from neo_tracker.helpers.neo_table import NeoTable
from neo_tracker.services import near_earth_object_fetcher_service


@require_http_methods(['GET'])
def index(request):
    try:
        start_date = get_start_date(request)
        end_date = get_end_date(request)
        validate_time_continuum(end_date, start_date)
    except ValueError as error:
        messages.error(request, error)
        return render(request, 'neo_tracker/index.html')

    try:
        near_earth_objects = near_earth_object_fetcher_service.get_objects(start_date=start_date, end_date=end_date)
    except HTTPError as error:
        messages.error(request, error)
        return render(request, 'neo_tracker/index.html')

    table = NeoTable(near_earth_objects)
    RequestConfig(request).configure(table)
    return render(request, 'neo_tracker/index.html', context={
        'table': table
    })
