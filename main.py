# Made by EK-Team
from cinemas.update_cinemas import update_cinemas
from genres.update_genres import update_genres
from movies.update_movies import update_movies
from sessions.fake_sessions import post_fake_sessions


def main():
    # Cinemas
    update_cinemas()

    # Genres
    update_genres()

    # Movies
    update_movies()

    # Sessions
    # post_fake_sessions("week")
    post_fake_sessions(adding_type="day")


if __name__ == '__main__':
    main()
