from cinemas.cinema_images import update_cinema_images
from cinemas.cinemas_info import update_cinemas_info


def update_cinemas():
    # Unique cinema keys list
    place_ids = ["ChIJl3xz8QnnOkcReSOln9d6RqY",
                 "ChIJ4dGDScndOkcRK6iYsuY5rCk",
                 "ChIJif8CqgvdOkcRxDok8ta8w7Y",
                 "ChIJG3CADybmOkcRkBn2_jOgbyA",
                 "ChIJjW4PlXLdOkcRH4w0juRF9Ww",
                 "ChIJ3X6gOm3oOkcRirf_eSmxXSI"]

    update_cinemas_info(place_ids)
    update_cinema_images(place_ids)


if __name__ == '__main__':
    update_cinemas()
