# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime


# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

# 1. Get the 40 most significant seismic events, and sort them by recency
def getSignificance(q):
    significance = q["properties"]["sig"]
    if significance is None:
        significance = 0
    return int(significance)

def getTime(dataitem):
    t = dataitem["properties"]["time"]
    if (t is None):
        t = 0
    return t


top40events = sorted(data["features"], key=getSignificance, reverse=True)[:40]
top40events.sort(key=getTime, reverse=True)

# 2. Simplify data and put in csv. Make date correct format. Create google maps-link
# Link format: https://www.google.com/maps/search/?api=1&query=latitude,longitude
header = ["Magnitude", "Place", "Felt Reports", "Date", "Link"]
rows = []

for q in top40events:
    clong, clat = q["geometry"]["coordinates"][0], q["geometry"]["coordinates"][1]
    rows.append([
        q["properties"]["mag"],
        q["properties"]["place"],
        0 if q["properties"]["felt"] is None else event["properties"]["felt"],
        str(datetime.date.fromtimestamp(
            int(q["properties"]["time"])/1000)),
        f'https://www.google.com/maps/search/?api=1&query={clat}%2C{clong}'
    ])

with open("Start/Ch_3/significantevents.csv", "w") as outputcsv:
    writer = csv.writer(outputcsv, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)