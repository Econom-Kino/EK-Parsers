import datetime
import time
import requests
from random import randint

from const import EK_IN_ROLLING_API, EK_SESSIONS_API, PLACE_IDs

TECHNOLOGIES = ['2D', '3D', '4DX']


# day_from: 0 - today, 1 - tomorrow
def generate_rand_sessions_for_movie(movie_id, day_from, num_of_days):
    sessions = []
    for day in range(day_from, day_from+num_of_days):
        for _ in range(randint(10, 14)):
            sessions.append({
                "cinema": PLACE_IDs[randint(0, 5)],
                "movie": movie_id,
                "price": randint(10, 25) * 5,
                "start_time": str(datetime.date.today() + datetime.timedelta(days=day)) + "T" + str(randint(8, 23)) + ":00:00+03:00",
                "ticket_link": "https://www.google.com",
                "language": "Українська",
                "technology": TECHNOLOGIES[randint(0, 2)]
            })
    return sessions


def post_fake_sessions(adding_type):
    day_from: int
    num_of_days: int

    if adding_type == "week":
        day_from = 0
        num_of_days = 6
    elif adding_type == "day":
        day_from = 7
        num_of_days = 1
    else:
        print("post_fake_sessions: wrong adding_type")

    movies_in_rolling = requests.get(EK_IN_ROLLING_API)

    for movie in movies_in_rolling.json():
        sessions = generate_rand_sessions_for_movie(movie['id'], day_from, num_of_days)
        for session in sessions:
            print(session)

        post = requests.post(EK_SESSIONS_API, json=sessions)
        print(post)
        print()