from cinemas.cinemas_info import update_cinemas_info


def update_cinemas():
    # Список кінотеатрів
    place_ids = open('cinemas/cinema_place_ids.txt', 'r').read().split('\n')

    update_cinemas_info(place_ids)


if __name__ == '__main__':
    update_cinemas()