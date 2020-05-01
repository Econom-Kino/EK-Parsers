# Made by EK-Team
from logs import write_log
from cinemas.update_cinemas import update_cinemas
from genres.update_genres import update_genres
from movies.update_movies import update_movies
from sessions.fake_sessions import post_fake_sessions


def main():
    # Cinemas
    try:
        update_cinemas()
    except:
        write_log("update_cinemas() error")
        print("update_cinemas() error")

    # Genres
    try:
        update_genres()
    except:
        write_log("update_cinemas() error")
        print("update_cinemas() error")

    # Movies
    try:
        update_movies()
    except:
        write_log("update_movies() error")
        print("update_movies() error")

    # Sessions
    try:
        # post_fake_sessions("week")
        post_fake_sessions(adding_type="day")
    except:
        write_log("post_fake_sessions() error")
        print("post_fake_sessions() error")


if __name__ == '__main__':
    main()
