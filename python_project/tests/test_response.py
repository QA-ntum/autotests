import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
token = '9061f47fe14f15b5cd7a8ed378576fa2'
header = {'Content-Type':'application/json', 'trainer_token': token}
trainer_id = '18025'

def test_homework():
    # response = requests.get(url= url, )
    response = requests.get(url= f'{url}/trainers', headers= header)
    assert response.status_code == 200

def test_homework_2():
    # response = requests.get(url= url, )
    response = requests.get(url= f'{url}/trainers?trainer_id=18025', headers= header)
    assert response.json()['data'][0]['trainer_name'] == 'Иннокентий'




