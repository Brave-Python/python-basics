""" je importeer de json-module die standaard in de Python-bibliotheek zit.
De basisbewerking bij JSON-parsing is het omzetten van een JSON-string 
naar een Python-gegevensstructuur waarmee je kunt werken. 
Zo voer je deze basisconversie uit
 """
import json

json_string = '{"name": "Brave Jongen", "age": 49, "city": "Zoetermeer"}'
person = json.loads(json_string)

print(person["name"]) 
print(person["age"])   
print(person["city"])
print(type(person))
