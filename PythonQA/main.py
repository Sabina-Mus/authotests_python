import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '071e5f945cf210cae61ea4e77bf89c62'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 100
}

body_name = {
    "pokemon_id": "72131",
    "name": "ПУпсик",
    "photo_id": 456
}

body_pokemon_id = {
    "pokemon_id": "72131"
}




'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create )
print(response_create.text)

message = response_create.json()['message']
print(message)'''

'''response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name )
print(response_create.text)'''

'''response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemon_id )
print(response_create.text)'''