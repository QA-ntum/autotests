import requests
from PIL import Image
from io import BytesIO

start_picture = 1000

min_width, min_height = 450, 450
max_width, max_height = 475, 475

def test_check_image_size(min_width, min_height, max_width, max_height):
    global start_picture
    while True:
        try:
            url = f'https://storage.yandexcloud.net/qastudio/pokemon_battle/pokemons/{start_picture}.png'
            response = requests.get(url)
            response.raise_for_status()

            image = Image.open(BytesIO(response.content))
            width, height = image.size
            if min_width <= width <= max_width and min_height <= height <= max_height:
                print(f'Изображение {url} корректно')
            else:
                print(f'Изображение {url} не корректно| текущий размер {width}x{height}')

            start_picture = start_picture + 1

        except Exception as e:
            print(f'Вероятно изображения закончились: {e}') # Ожидаю что 404 получаю по причине отсутствия картинки
            break # и прерываю цикл

test_check_image_size(min_width, min_height, max_width, max_height)

