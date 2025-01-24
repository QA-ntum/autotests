import requests
from PIL import Image
from io import BytesIO
import pytest

start_picture = 1000

min_width, min_height = 450, 450
max_width, max_height = 475, 475

list_of_numbers = []

for i in range(0, 2): # тут вообще (100,1009) но мне реализация такая не нравится, надо что бы он сам понимал когда начать и остановиться
    list_of_numbers.append(100+i)

@pytest.mark.parametrize('end_point', list_of_numbers)

def test_picture_size(end_point):
    url = f'https://storage.yandexcloud.net/qastudio/pokemon_battle/pokemons/{end_point}.png'
    response = requests.get(url)
    response.raise_for_status()

    image = Image.open(BytesIO(response.content))

    width, height = image.size
    assert min_width <= width <= max_width and min_height <= height <= max_height

