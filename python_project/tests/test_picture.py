import requests
from PIL import Image
from io import BytesIO
import pytest

first_picture = 1000                # С какой картинки начинаем проверять
last_picture = 1008                 # По какую включительно
min_width, min_height = 450, 450    # Минимальное допустимое значение
max_width, max_height = 475, 475    # Максимальное допустимое значение

list_of_numbers = []

# Костальная реализация параметризации :D

for i in range(first_picture, last_picture): 
    list_of_numbers.append(i)

@pytest.mark.parametrize('end_point', list_of_numbers)

def test_picture_size(end_point):

    if end_point < 100:
        formatted_value = f"{end_point:03}"
    else:
        formatted_value = str(end_point)

    url = f'https://storage.yandexcloud.net/qastudio/pokemon_battle/pokemons/{formatted_value}.png'
    response = requests.get(url)
    response.raise_for_status()

    image = Image.open(BytesIO(response.content))
    width, height = image.size
    assert min_width <= width <= max_width and min_height <= height <= max_height
