import requests

from const import GENRES_REQUEST, EK_GENRES_API


def update_genres():
    # Get genres from TMDb
    tmdb_genres = requests.get(GENRES_REQUEST).json()

    for genre in tmdb_genres['genres']:
        local_genre_request = EK_GENRES_API + '/' + str(genre['id'])
        local_genre = requests.get(local_genre_request)

        # dict that will PUT/POST to EK_API
        genre_data = {'name': genre['name'],
                      'pseudo_id': genre['id']}

        # Check if genre exist in our db
        # If exist (status_code == 200), than refresh (PUT)
        # If not exist (status_code == 404), than add new (POST)
        if local_genre.status_code == 200:
            put = requests.put(local_genre_request, data=genre_data)
            print('Genre ' + genre_data['name'] + ': PUT request:', put.status_code)
        elif local_genre.status_code == 404:
            post = requests.post(EK_GENRES_API, data=genre_data)
            print('Genre ' + genre_data['name'] + ': POST request:', post.status_code)
        else:
            print("update_genres: Something goes ne tak")
