from movies.movies import update_films
from const import UPCOMING, NOW_PLAYING


def update_movies():
    try:
        update_films(UPCOMING)
    except:
        print("update_movies(): Upcoming error")

    try:
        update_films(NOW_PLAYING)
    except:
        print("update_movies(): now playing error")
