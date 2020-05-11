import requests

from keys import GOOGLE_API_KEY
from const import EK_CINEMA_IMAGES_API, CINEMA_PHOTOS_API, CINEMA_DETAILS_API, EK_CINEMAS_API


# POST request EK API to add new photos
# @param: img_to_post - set with photo links that must be posted
# @param: place_id - unique cinema key
def post_cinema_photos(img_to_post, place_id):
    for img in img_to_post:
        data = [{
            'cinema': place_id,
            'image_link': img
        }]
        post = requests.post(EK_CINEMA_IMAGES_API, json=data)
        print('Images POST request:', post.status_code, post.json())
    print()


# Func deletes cinema photos in our db
# @param: num_to_delete - number of photos that must be deleted
# @param: place_id - unique cinema key
def delete_local_cinema_photos(num_to_delete, place_id):
    local_cinema_photos_request = EK_CINEMAS_API + '/' + place_id + '/cinema-images'

    for count, photo in enumerate(requests.get(local_cinema_photos_request).json()):
        if count == num_to_delete:
            break

        photo_to_del_request = EK_CINEMA_IMAGES_API + '/' + str(photo['id'])
        delete = requests.delete(photo_to_del_request)

        print("delete_local_cinema_photos: ", delete)


# Func returns set with photo links that exist in our db
# @param: place_id - unique cinema key
def get_local_cinema_photos(place_id):
    local_cinema_photos = set()
    local_cinema_photos_request = EK_CINEMAS_API + '/' + place_id + '/cinema-images'

    for photo in requests.get(local_cinema_photos_request).json():
        local_cinema_photos.add(photo['image_link'])

    return local_cinema_photos


# Func returns set with photo links of cinema
# @param: photo_references - photo keys in GOOGLE API, by which will retrieve photo links
def get_cinema_photos(photo_references):
    parsed_photos = set()

    for count, photo in enumerate(photo_references):
        cinema_photo_request = CINEMA_PHOTOS_API + photo['photo_reference'] + '&key=' + GOOGLE_API_KEY
        photo_link = requests.get(cinema_photo_request)
        parsed_photos.add(photo_link.url)

        if count == 5:
            break

    return parsed_photos


# Func refresh cinema images
# @param: place_ids - unique cinema keys list
def update_cinema_images(place_ids):
    for place_id in place_ids:
        # GET request to  GOOGLE API to retrieve photo keys (photo_references)
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
