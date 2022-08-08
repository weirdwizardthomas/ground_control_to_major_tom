# Near Earth object tracker

This repository houses a simple Django app to track near Earth objects.

## Assignment

Write a simple server providing a web page that takes two date arguments and retrieves the list of near-Earth space
objects approaching Earth in that time interval. Display the list of the objects, sorted by their closest approach
distance, in an aligned tabular format, the object name, size estimate, time and distance of the closest encounter.

The data should come from the API of NeoWs service at https://api.nasa.gov/ (free registration required).


## Run

### NASA NeoWs API

An API key is required.

1. Follow the instructions at https://api.nasa.gov/ to obtain your API key.
2. create `.env'` in project's root.
3. create a variable `API_KEY=$your api key$` in `.env`.

### Heroku

The app is hosted on [Heroku](https://dashboard.heroku.com/): https://ground-control-neows.herokuapp.com/app/. The deployed version is also a part of this repository, in a separate branch `heroku-deploy`, containing additional changes needed for Heroku deployment.

