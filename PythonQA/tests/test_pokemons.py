import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '071e5f945cf210cae61ea4e77bf89c62'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

TRAINER_ID = '5269'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

@pytest.mark.parametrize ('key, value', [('trainer_id', TRAINER_ID)])
def test_parametrize(key, value)
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
