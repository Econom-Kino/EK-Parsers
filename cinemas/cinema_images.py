import requests

from keys import GOOGLE_API_KEY
from const import EK_CINEMA_IMAGES_API, CINEMA_PHOTOS_API, CINEMA_DETAILS_API


# POST запит до EK API для додавання нових фото
def post_cinema_photos(img_to_post, place_id):
    for img in img_to_post:
        data = {
            'cinema': place_id,
            'image_link': img
        }
        post = requests.post(EK_CINEMA_IMAGES_API, data=data)
        print('Images POST request:', post.status_code)
    print()


def delete_local_cinema_photos(num_to_delete, place_id):
    local_cinema_photos_request = EK_CINEMA_IMAGES_API + 'cinema/' + place_id + '/'

    for count, photo in enumerate(requests.get(local_cinema_photos_request).json()):
        if count == num_to_delete:
            break

        photo_to_del_request = EK_CINEMA_IMAGES_API + 'id/' + str(photo['id']) + '/'
        delete = requests.delete(photo_to_del_request)

        print("delete_local_cinema_photos: ", delete)


# Функція повертає сет з силками на фото кінотеатрів, що є у нашій базі
def get_local_cinema_photos(place_id):
    local_cinema_photos = set()
    local_cinema_photos_request = EK_CINEMA_IMAGES_API + 'cinema/' + place_id + '/'

    for photo in requests.get(local_cinema_photos_request).json():
        local_cinema_photos.add(photo['image_link'])

    return local_cinema_photos


# Функція повертає сет з силками на фото кінотеатру
# @param: photo_references ключі фіотографій в GOOGLE API, за допомогою яких можна отримати посилання на самі фото
def get_cinema_photos(photo_references):
    parsed_photos = set()

    for count, photo in enumerate(photo_references):
        cinema_photo_request = CINEMA_PHOTOS_API + photo['photo_reference'] + '&key=' + GOOGLE_API_KEY
        photo_link = requests.get(cinema_photo_request)
        parsed_photos.add(photo_link.url)

        if count == 5:
            break

    return parsed_photos


# Функція оновлює фото кінотеатрів
# @param: place_ids - список кінотеатрів
def update_cinema_images(place_ids):
    for place_id in place_ids:
        # GET запит до  GOOGLE API для отроимання ключів фотографій (photo_references)
        photo_references_request = CINEMA_DETAILS_API + 'place_id=' + place_id + '&fields=photos&key=' + GOOGLE_API_KEY
        photo_references = requests.get(photo_references_request).json()['result']['photos']

        local_cinema_photos = get_local_cinema_photos(place_id)

        if len(local_cinema_photos) == 6:
            img_to_post = get_cinema_photos(photo_references) - local_cinema_photos
            print("Images to POST:", img_to_post)

            delete_local_cinema_photos(len(img_to_post), place_id)
            post_cinema_photos(img_to_post, place_id)
        else:
            img_to_post = get_cinema_photos(photo_references)
            print("Images to POST:", img_to_post)

            delete_local_cinema_photos(len(local_cinema_photos), place_id)
            post_cinema_photos(img_to_post, place_id)
