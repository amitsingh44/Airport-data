import json

with open("airports.json") as json_file:
    airports = json.load(json_file)

with open("airport_data.json") as json_file:
    data = json.load(json_file)

dictOne = {}
dictTwo = {}

for i in (airports): # Airport
    dictOne[i["icao"]] = i

for i in (data): # Data
   dictTwo[str(i["icao"])] = i

# print(dictTwo)

for k,v in dictTwo.items():
    # print(k)
    if k in dictOne:
        dictTwo[k]['elevation_feet'] = dictOne[k]['elevation_ft']
        dictTwo[k]['wikipedia_link'] = dictOne[k]['wikipedia_link']
        dictTwo[k]['latitude'] = float(dictOne[k]['latitude_deg'])
        dictTwo[k]['longitude'] = float(dictOne[k]['longitude_deg'])
        # print(dictTwo[k])
    # else:
    #     dictTwo[k]['elevation_feet'] = None
    #     dictTwo[k]['wikipedia_link'] = None


print(dictTwo)

file = open("data.json","a")
file.write(json.dumps(dictTwo))
file.close()
