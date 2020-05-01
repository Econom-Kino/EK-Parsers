from cinemas.cinema_images import update_cinema_images
from cinemas.cinemas_info import update_cinemas_info


def update_cinemas():
    # Unique cinema keys list
    place_ids = open('cinemas/cinema_place_ids.txt', 'r').read().split('\n')

    update_cinemas_info(place_ids)
    update_cinema_images(place_ids)


if __name__ == '__main__':
    update_cinemas()
