import datetime
from random import randint
import requests

from const import EK_IN_ROLLING_API, EK_SESSIONS_API


TECHNOLOGIES = ['2D', '3D', '4DX']
place_ids = open('../cinemas/cinema_place_ids.txt', 'r').read().split('\n')


def generate_rand_sessions_for_movie(movie_id):
    sessions = []
    for day in range(7):
        for _ in range(randint(10, 15)):
            sessions.append({
                'cinema': place_ids[randint(0, 5)],
                'movie': movie_id,
                'price': randint(10, 25) * 5,
                'start_time': str(datetime.date.today() + datetime.timedelta(days=day)) + "T" + str(randint(8, 23)) + ":00:00+03:00",
                "ticket_link": "https://www.google.com",
                "language": "Українська",
                "technology": TECHNOLOGIES[randint(0, 2)]
            })
    return sessions


def post_fake_sessions():
    movies_in_rolling = requests.get(EK_IN_ROLLING_API)

    for movie in movies_in_rolling.json():
        sessions = generate_rand_sessions_for_movie(movie['id'])
        for session in sessions:
            print(session)
            post = requests.post(EK_SESSIONS_API, data=session)
            print(post)


if __name__ == '__main__':
    post_fake_sessions()