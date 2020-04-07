import requests

from keys import GOOGLE_API_KEY
from const import EK_CINEMA_IMAGES_API, CINEMA_PHOTOS_API, EK_CINEMAS_API, CINEMA_DETAILS_API


# Функція повертає сет з силками на фото кінотеатрів, що є у нашій базі
def get_local_cinema_photos():
    local_cinema_photos = set()

    for link in requests.get(EK_CINEMA_IMAGES_API).json():
        local_cinema_photos.add(link['image_link'])
    return local_cinema_photos


# Функція повертає сет з силками на фото кінотеатру
# @param: photo_references ключі фіотографій в GOOGLE API, за допомогою яких можна отримати посилання на самі фото
def get_cinema_photos(photo_references):
    parsed_photos = set()

    for photo in photo_references:
        cinema_photo_request = CINEMA_PHOTOS_API + photo['photo_reference'] + '&key=' + GOOGLE_API_KEY

        photo_link = requests.get(cinema_photo_request)
        parsed_photos.add(photo_link.url)

    return parsed_photos


# Функція оновлює фото кінотеатрів
# @param: place_ids - список кінотеатрів
def update_cinema_images(place_ids):
    for place_id in place_ids:
        # GET запит до EK API для отримання id поточного кінотеатру
        cinema_request = EK_CINEMAS_API + place_id + '/'
        cinema = requests.get(cinema_request)

        # GET запит до  GOOGLE API для отроимання ключів фотографій (photo_references)
        photo_references_request = CINEMA_DETAILS_API + 'place_id=' + place_id + '&fields=photos&key=' + GOOGLE_API_KEY
        photo_references = requests.get(photo_references_request).json()['result']['photos']

        # POST запит до EK API для додавання нових фото
        if cinema.status_code == 200:
            img_to_post = get_cinema_photos(photo_references) - get_local_cinema_photos()
            # print("Images to POST:", img_to_post)

            for img in img_to_post:
                data = {
                    'cinema': cinema.json()['id'],
                    'image_link': img
                }
                post = requests.post(EK_CINEMA_IMAGES_API, data=data)
                print(cinema.json()['name'] + ': Images POST request:', post.status_code)
        else:
            print("update_cinema_images: Something goes ne tak")
        print()
