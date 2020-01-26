#!/usr/bin/env python

# Script to convert JSON weather data into
# a format suitable for transmissting via APRS
# 
# Dana Simmons 2019

import requests


WEATHER_STATION_ADDRESS = "http://10.1.1.252/i"

resp = requests.get(WEATHER_STATION_ADDRESS)
data = resp.json()
temperature = int(data['temperature'])
humidity = int(data['humidity'])
pressure = int(data['pressure'])

wxnow_str = (f'000/000g000t{temperature}r000p000P000h{humidity}b{pressure}')

print(wxnow_str)