# Near Earth object tracker

This repository houses a simple Django app to track near Earth objects.

## Assignment

Write a simple server providing a web page that takes two date arguments and retrieves the list of near-Earth space
objects approaching Earth in that time interval. Display the list of the objects, sorted by their closest approach
distance, in an aligned tabular format, the object name, size estimate, time and distance of the closest encounter.

The data should come from the API of NeoWs service at https://api.nasa.gov/ (free registration required).

## Installation

1. Download the project:

```shell
git clone https://github.com/weirdwizardthomas/ground_control_to_major_tom
cd ground_control_to_major_tom
```

2. Set up Python and get packages (creating a [virtual environment](https://docs.python.org/3/library/venv.html) is
   strongly recommended):

```shell
python -m pip install -r requirements.txt
```

3. Run the initial Django migration:

```shell
python manage.py makemigrations
python manage.py migrate
```

### NASA NeoWs API

An API key is required.

1. Follow the instructions at https://api.nasa.gov/ to obtain your API key.
2. create `.env` in project's root.
3. create a variable `NASA_API_KEY=$your nasa  api key$` in `.env`.

### Run

After installing, run

```shell
python manage.py runserver
```

### Heroku

The app is hosted on [Heroku](https://dashboard.heroku.com/): https://ground-control-neows.herokuapp.com/app/. The
deployed version is also a part of this repository, in a separate branch `heroku-deploy`, containing additional changes
needed for Heroku deployment.

