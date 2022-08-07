import itertools
from datetime import datetime

import requests

from neo_tracker.models import NearEarthObject

API_KEY = ... # todo put api key here
URL = 'https://api.nasa.gov/neo/rest/v1/feed'


def flatten_list(data):
    # https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
    return list(itertools.chain.from_iterable(data))


def handle_status_code(status_code):
    # todo
    pass


def get_objects(start_date=datetime.now(), end_date=None):
    params = {'start_date': start_date,
              'end_date': end_date,
              'api_key': API_KEY}

    response = requests.get(URL, params=params)
    handle_status_code(status_code=response.status_code)
    data = response.json()['near_earth_objects'].values()

    return [NearEarthObject.from_dictionary(x) for x in flatten_list(data)]


def sort_by_miss_distance(near_earth_object):
    return near_earth_object.miss_distance()

