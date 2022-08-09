import itertools
import requests
from datetime import datetime

import pandas as pd

from django.conf import settings
from django.contrib import messages
from requests import HTTPError

from neo_tracker.models import NearEarthObject

URL = 'https://api.nasa.gov/neo/rest/v1/feed'


def flatten_list(data):
    # https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
    return list(itertools.chain.from_iterable(data))


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


def as_dataframe(start_date=datetime.now(), end_date=None):
    neos = sorted(get_objects(end_date), key=sort_by_miss_distance)
    df = pd.DataFrame(neos)
    return df.to_html()
