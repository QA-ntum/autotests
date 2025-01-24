import requests
import time

# Само собой тут ещё можно огромное кол-во исключений и отказоустойчивости добавить, но мне лучше сконцентрироваться на обучении в других аспектах :D

url = 'https://api.pokemonbattle.ru/v2'
token = '9061f47fe14f15b5cd7a8ed378576fa2'
header = {'Content-Type':'application/json', 'trainer_token': token}
trainer_id = '18025'

# Генерим покемона

body = {
    "name": "Пабиждатор 9000",
    "photo_id": -1
}

response = requests.post(url= f'{url}/pokemons', headers = header, json=body)
response.raise_for_status()

pokemon_id = response.json()['id'] # Фиксируем айдишник

# Даём ему более скромное имя
body_rename = {
    "pokemon_id": f'{pokemon_id}',
    "name": "generate",
}

response = requests.patch(url= f'{url}/pokemons', headers= header, json= body_rename) # Да, я знаю что в задании было put
response.raise_for_status()


# Ловим нашего гладиатора в шар

body_catch = {

    "pokemon_id": f'{pokemon_id}'
}


response = requests.post(url= f'{url}/trainers/add_pokeball', headers= header, json= body_catch)
response.raise_for_status()

crutch = 0 # Наверняка можно было лучше оптимизировать, но мне лень :)

while crutch != "Твой покемон проиграл":
    
    try:
        # Ищем супостата
        response = requests.get(url= f'{url}/pokemons?=in_pokeball=1&status=1', headers= header)

        for i in range(len(response.json()['data'])):
            if response.json()['data'][i]['trainer_id'] != f'{trainer_id}':
                enemy_id = response.json()['data'][i]['id'] # Фиксируем айдишник вражины
                break

            
    
        # Драка смертоубийственная
        body_fight = {

        "attacking_pokemon": f'{pokemon_id}',
        "defending_pokemon": f'{enemy_id}'

        }

        
        response = requests.post(url= f'{url}/battle', headers= header, json= body_fight)
        response.raise_for_status()

        crutch = response.json()["result"]
        print(f'{crutch} | Осталось боёв {response.json()["battle_limit"]}')
        
    except Exception as e:
        print(f'Ошибочка вышла {e}')
        time.sleep(60)

# Закономерный итог
print(f'Жил без страха и нокаутировался без страха')
