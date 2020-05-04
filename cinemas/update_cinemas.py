from cinemas.cinema_images import update_cinema_images
from cinemas.cinemas_info import update_cinemas_info
from const import PLACE_IDs


def update_cinemas():
    update_cinemas_info(PLACE_IDs)
    update_cinema_images(PLACE_IDs)


if __name__ == '__main__':
    update_cinemas()
