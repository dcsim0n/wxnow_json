#!/usr/bin/env python

# Script to convert JSON weather data into
# a format suitable for transmissting via APRS
# 
# Dana Simmons 2020

import sys,json

data = json.load(sys.stdin)

temperature = int(data['temperature'])
humidity = int(data['humidity'])
pressure = int(data['pressure'])

wxnow_str = (f'000/000g000t{str(temperature).zfill(3)}r000p000P000h{humidity}b{pressure}')

print(wxnow_str)