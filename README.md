# Near Earth object tracker

This repository houses a simple Django app to track near Earth objects.

## Assignment

Write a simple server providing a web page that takes two date arguments and retrieves the list of near-Earth space
objects approaching Earth in that time interval. Display the list of the objects, sorted by their closest approach
distance, in an aligned tabular format, the object name, size estimate, time and distance of the closest encounter.

The data should come from the API of NeoWs service at https://api.nasa.gov/ (free registration required).

## To-do

* [ ] write the app
* [ ] write a run guide
    * [x] api key
    * [ ] create a setup script, which also creates the `keychain.py` file
    * [ ] installing
* [ ] host the app

## Run

### NASA NeoWs API

An API key is required.

1. Follow the instructions at https://api.nasa.gov/ to obtain your API key
2. create a file `ground_control\keychain.py`
3. create a variable `API_KEY=$your api key$`