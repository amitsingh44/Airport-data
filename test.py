import json

data = [
    {
        "id": 1,
        "iata": "XYZ",
        "icao": "ABCD",
        "size": 5,
        "type": "medium_airport",
        "name": "Test 1",
        "elevation_feet": ""
    },
    {
        "id": 2,
        "iata": "UVW",
        "icao": "EFGH",
        "size": 5,
        "type": "medium_airport",
        "name": "Test 2",
        "elevation_feet": ""
    },
    {
        "id": 3,
        "iata": "RST",
        "icao": "IJKL",
        "size": 5,
        "type": "medium_airport",
        "name": "Test 3",
        "elevation_feet": ""
    },
    {
        "id": 4,
        "iata": "OPQ",
        "icao": "MNOP",
        "size": 5,
        "type": "medium_airport",
        "name": "Test 4",
        "elevation_feet": ""
    },
    {
        "id": 5,
        "iata": "LMN",
        "icao": "QRST",
        "size": 5,
        "type": "medium_airport",
        "name": "Test 5",
        "elevation_feet": ""
    },
    {
        "id": 6,
        "iata": "UVW",
        "icao": "ABCD",
        "size": 5,
        "type": "medium_airport",
        "name": "Test 6",
        "elevation_feet": ""
    }
]

airports = [
    {
        "id": 1,
        "ident": "ABCD",
        "type": "medium_airport",
        "name": "Test 1",
        "icao": "ABCD",
        "iata_code": "UVW",
        "elevation": 123
    },
    {
        "id": 2,
        "ident": "EFGH",
        "type": "medium_airport",
        "name": "Test 2",
        "icao": "EFGH",
        "iata_code": "XYZ",
        "elevation": 114
    },
    {
        "id": 3,
        "ident": "IJKL",
        "type": "medium_airport",
        "name": "Test 3",
        "icao": "IJKL",
        "iata_code": "RST",
        "elevation": 456
    },
    {
        "id": 4,
        "ident": "MNOP",
        "type": "medium_airport",
        "name": "Test 4",
        "icao": "MNOP",
        "iata_code": "DEO",
        "elevation": 789
    },
    {
        "id": 5,
        "ident": "QRST",
        "type": "medium_airport",
        "name": "Test 5",
        "icao": "QRST",
        "iata_code": "MQL",
        "elevation": 101
    },
    {
        "id": 6,
        "ident": "UVWX",
        "type": "medium_airport",
        "name": "Test 6",
        "icao": "UVWX",
        "iata_code": "CDE",
        "elevation": 112
    },
]

show = []

for i in data:
    for j in airports:
        if i["iata"] == j["iata_code"] and i["icao"] == j["icao"]:
            file = open("test.json","a")
            print(f"{i['id']} is Completed")
            show.append(

                {
                    "iata": j["iata_code"],
                    "icao": j["icao"],
                    "size": 5,
                    "type": "medium_airport",
                    "name": j["name"],
                    "elevation_feet": j["elevation"]
                }
            )
            file.write(json.dumps(show))
            file.close()

print(show)