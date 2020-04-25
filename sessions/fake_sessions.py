import datetime
from random import randint
import requests

from const import EK_IN_ROLLING_API, EK_SESSIONS_API


TECHNOLOGIES = ['2D', '3D', '4DX']
place_ids = open('../cinemas/cinema_place_ids.txt', 'r').read().split('\n')


# day_from: 0 - today, 1 - tomorrow
def generate_rand_sessions_for_movie(movie_id, day_from, num_of_days):
    sessions = []
    for day in range(day_from, day_from+num_of_days):
        for _ in range(randint(10, 14)):
            sessions.append({
                "cinema": place_ids[randint(0, 5)],
                "movie": movie_id,
                "price": randint(10, 25) * 5,
                "start_time": str(datetime.date.today() + datetime.timedelta(days=day)) + "T" + str(randint(8, 23)) + ":00:00+03:00",
                "ticket_link": "https://www.google.com",
                "language": "Українська",
                "technology": TECHNOLOGIES[randint(0, 2)]
            })
    return sessions


def post_fake_sessions(day_from, num_of_days):
    movies_in_rolling = requests.get(EK_IN_ROLLING_API)

    for movie in movies_in_rolling.json():
        sessions = generate_rand_sessions_for_movie(movie['id'], day_from, num_of_days)
        for session in sessions:
            print(session)

        post = requests.post(EK_SESSIONS_API, json=sessions)
        print(post)
        print()


if __name__ == '__main__':
    post_fake_sessions(day_from=0, num_of_days=7)
