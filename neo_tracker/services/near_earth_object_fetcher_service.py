from datetime import datetime

import requests
from django.conf import settings

from neo_tracker.models import NearEarthObject
from neo_tracker.util import flatten_list

URL = 'https://api.nasa.gov/neo/rest/v1/feed'


def get_objects(start_date=datetime.now(), end_date=None):
    params = {'start_date': start_date,
              'end_date': end_date,
              'api_key': settings.NASA_API_KEY}

    response = requests.get(URL, params=params)
    response.raise_for_status()

    data = response.json()['near_earth_objects'].values()

    return [NearEarthObject.from_dictionary(x) for x in flatten_list(data)]


def sort_by_miss_distance(near_earth_object):
    return near_earth_object.miss_distance()
