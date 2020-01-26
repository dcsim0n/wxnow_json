#!/bin/bash

# Shell script to fetch data from weather station
# pipe data into python script and format the data
#
# Dana Simmons 2020

WEATHER_STATION="http://10.1.1.252"

curl -s $WEATHER_STATION | python3 app.py