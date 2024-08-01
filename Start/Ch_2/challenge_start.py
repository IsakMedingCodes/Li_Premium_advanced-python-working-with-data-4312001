# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import Counter


# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

events = data["features"]

c=Counter([e["properties"]["type"] for e in events])

print(c)
print(f'earthquake      : {c["earthquake"]}')
print(f'explosion       : {c["explosion"]}')
print(f'quarry blast    : {c["quarry blast"]}')
print(f'ice quake       : {c["ice quake"]}')
print(f'other event     : {c["other event"]}')