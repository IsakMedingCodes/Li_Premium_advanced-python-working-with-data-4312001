# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json

# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Solution:
# 1. total number of quakes
nbEvents = len(data["features"])

# 2. number of quakes with at least 100 reports
def filterAtLeast100(q):
    if q["properties"]["felt"] is not None and q["properties"]["felt"] >= 100:
        return True
    return False

# 3. the quake felt by the highest number of people
def getFelt(q):
    felt = q["properties"]["felt"]
    if felt is None:
        felt = 0
    return int(felt)

def quakeToString(q, felt=False, sig=False): # helper function for pretty printing
    result = f'M {"{:.1f}".format(q["properties"]["mag"])} - {q["properties"]["place"]}'
    if felt:
        result = result + f', reports: {q["properties"]["felt"]}'
    if sig:
        result = result + f', Significance: {q["properties"]["sig"]}'
    return result
    
mostfelt = max(data["features"], key=getFelt)

# 4. Get top 10 most significant events
def getSignificance(q):
    significance = q["properties"]["sig"]
    if significance is None:
        significance = 0
    return int(significance)

topsig = sorted(data["features"], key=getSignificance, reverse=True)

#top10quakessig = sorted(data["features"])
# The print
print(f'Total quakes: {nbEvents}')
print(f'Total quakes felt by at least 100 people: {len(list(filter(filterAtLeast100,data["features"])))}')
print(f'Most felt reports: {quakeToString(mostfelt, felt=True)}')
print("The 10 most significant events were:")
for q in topsig[:10]:
    print(f'Event: {quakeToString(q, sig=True)}')