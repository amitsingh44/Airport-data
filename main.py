import json

with open("airports.json") as json_file:
    airports = json.load(json_file)

with open("airport_data.json") as json_file:
    data = json.load(json_file)


# result = []

for i in data:
    for j in airports:
        if (i["iata"] == j["iata_code"] or i["icao"]) == j["icao"] and i["icao"] != "" and j["icao"] != "":
            file = open("data.json","a")


            print(f"{i['id']} is Completed")

            # result.append(
            #     {
            #         "id": i["id"],
            #         "iata": j["iata_code"],
            #         "icao": j["icao"],
            #         "size": i["size"],
            #         "type": j["type"],
            #         "name": j["name"],
            #         "location": i["location"],
            #         "location_translations": (i["location_translations"]),
            #         "hero_image": "",
            #         "latitude": int(j["latitude_deg"]),
            #         "longitude": int(j["longitude_deg"]),
            #         "elevation_feet": j["elevation_ft"],
            #         "country": i["country"],
            #         "continent": i["continent"],
            #         "extra_content": i["extra_content"],
            #         "visibility": i["visibility"],
            #         "scheduled_service": i["scheduled_service"],
            #         "surface": i["surface"],
            #         "timezone": i["timezone"],
            #         "runway_length": i["runway_length"],
            #         "runway_width": i["runway_width"],
            #         "operating_hours": i["operating_hours"],
            #         "slot_sensitive": i["slot_sensitive"],
            #         "parking_sensitive": i["parking_sensitive"],
            #         "weather_sensitive": i["weather_sensitive"],
            #         "special_crew_training": i["special_crew_training"],
            #         "fire_category": i["fire_category"],
            #         "fc_upgrade_possible": i["fc_upgrade_possible"],
            #         "of_entry": i["of_entry"],
            #         "political_restrictions": i["political_restrictions"],
            #         "special_restrictions": i["special_restrictions"]
            #     }
            # )
     
            file.write(json.dumps(
                {
                    "id": i["id"],
                    "iata": j["iata_code"],
                    "icao": j["icao"],
                    "size": i["size"],
                    "type": j["type"],
                    "name": j["name"],
                    "location": i["location"],
                    "location_translations": (i["location_translations"]),
                    "hero_image": "",
                    "latitude": float(j["latitude_deg"]),
                    "longitude": float(j["longitude_deg"]),
                    "elevation_feet": j["elevation_ft"],
                    "country": i["country"],
                    "continent": i["continent"],
                    "extra_content": i["extra_content"],
                    "visibility": i["visibility"],
                    "scheduled_service": i["scheduled_service"],
                    "surface": i["surface"],
                    "timezone": i["timezone"],
                    "runway_length": i["runway_length"],
                    "runway_width": i["runway_width"],
                    "operating_hours": i["operating_hours"],
                    "slot_sensitive": i["slot_sensitive"],
                    "parking_sensitive": i["parking_sensitive"],
                    "weather_sensitive": i["weather_sensitive"],
                    "special_crew_training": i["special_crew_training"],
                    "fire_category": i["fire_category"],
                    "fc_upgrade_possible": i["fc_upgrade_possible"],
                    "of_entry": i["of_entry"],
                    "political_restrictions": i["political_restrictions"],
                    "special_restrictions": i["special_restrictions"],
                    "wikipedia_link": j["wikipedia_link"],
                }
            ))
            file.close()
print("*********************************************")
# print(result)


