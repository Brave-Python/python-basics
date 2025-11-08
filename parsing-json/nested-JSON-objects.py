
""" In dit voorbeeld vereist elk niveau van genesting een extra set vierkante haken. 
De expressie weather["location"]["city"] benadert eerst het object "location" en 
haalt vervolgens de waarde van "city" daaruit op. 
Je kunt zo diep gaan als nodig is, bijvoorbeeld weather["current"]["wind"]["speed_mph"], 
wat drie niveaus diep gaat. Deze kettingnotatie weerspiegelt precies 
hoe je de gegevens zou benaderen in de oorspronkelijke JSON-structuur.
 """
import json

weather_data = '''
{
    "location": {
        "city": "Seattle",
        "state": "WA",
        "coordinates": {
            "latitude": 47.6062,
            "longitude": -122.3321
        }
    },
    "current": {
        "temperature_f": 58,
        "conditions": "Partly Cloudy",
        "humidity": 72,
        "wind": {
            "speed_mph": 8,
            "direction": "NW"
        }
    }
}
'''

weather = json.loads(weather_data)

print(weather["location"]["city"])
print(weather["location"]["state"])
print(weather["current"]["temperature_f"])
print(weather["current"]["conditions"])

# Output via variabelen
city = weather["location"]["city"]
temp = weather["current"]["temperature_f"]
wind_speed = weather["current"]["wind"]["speed_mph"]

print(f"{city}: {temp}°F, Wind {wind_speed} mph")


