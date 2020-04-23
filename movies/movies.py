from time import perf_counter

from const import NOW_PLAYING, UPCOMING
from keys import TMDB_KEY, OMDB_KEY
import requests

start = perf_counter()

# path_before poster
path_before = 'http://image.tmdb.org/t/p/w600_and_h900_bestv2'


def get_pages(link):

    pageuk = requests.get(link+'&page=1')
    # transform request to json format
    pageuk = pageuk.json()
    # amount of pages
    nums_of_pages = pageuk['total_pages']
    return nums_of_pages


def get_IDlist(page,link):

    pageuk = requests.get(
        link+'&page=' + str(
            page) + '&region=UA')
    pageuk = pageuk.json()
    # pages
    res = ((pageuk['results']))

    # list of id from db
    films_id = []
    for film_id in res:
        films_id.append(film_id['id'])

    return films_id


def get_title(film_object):
    return film_object['title']


def get_trailer(flim_object, id):
    trailers_response = requests.get(
        'https://api.themoviedb.org/3/movie/' + str(id) + '/videos?api_key=' + TMDB_KEY + '&language=uk-UA')
    trailers = trailers_response.json()['results']
    try:
        trailer = 'https://www.youtube.com/watch?v=' + trailers[len(trailers) - 1]['key']
    except:
        trailer = None
    return trailer


def get_poster(film_object):
    poster_link = ''
    try:
        poster_link = path_before + film_object['poster_path']
    except:
        poster_link = 'https://i.imgur.com/CPBk3g2.png'
    return poster_link


def get_genres(film_object):
    list_of_genres = film_object['genres']
    genres = []
    for gan in list_of_genres:
        genres.append(gan['name'])
    return genres


def get_AgeLimit(film_object):
    return film_object['adult']


def get_imdbId(film_object):
    imdbID = ''
    try:
        if (film_object['imdb_id'] == ''):
            imdbID = None
        else:
            imdbID = film_object['imdb_id']
    except:
        imdbID = None
    return imdbID


def get_rating(film_object):
    rating = 0
    try:
        IMDB_rating = \
        requests.get('http://www.omdbapi.com/?i=' + film_object['imdb_id'] + '&apikey=' + OMDB_KEY).json()['imdbRating']
        IMDB_rating = (float(IMDB_rating))
        rating = IMDB_rating
    except:
        rating = None
    return rating


def get_duration(film_object):
    return int(film_object['runtime'])


def get_ReleaseDate(film_object):
    return film_object['release_date']


def get_local_actors():
    request_local_actors = requests.get('https://ekinoback.herokuapp.com/actors')
    actors_list = []
    for actor in request_local_actors.json():
        actors_list.append(actor['name'])
    return actors_list


def get_actors(id):
    # actors
    actors = []

    # request for info about
    act = requests.get('https://api.themoviedb.org/3/movie/' + str(
        id) + '/credits?api_key=' + TMDB_KEY + '&language=uk')

    list_actors_info = act.json()['cast']

    local_actors = get_local_actors()

    # take only 5 actors
    count =0
    for element in list_actors_info:
        if(count==5):
            break
        loc_dict_actor = {}

        # loc_dict_actors['character'] = element['character']
        loc_dict_actor['name'] = element['name']

        if (element['name'] not in local_actors):
            local_actors.append(element['name'])
            r = requests.post('https://ekinoback.herokuapp.com/actors', json=loc_dict_actor)

        actors.append(loc_dict_actor['name'])
        count+=1
    return actors


def get_country_production(film_object):
    # find all countries, and pass them to the list
    list_of_countries = film_object['production_countries']
    for i in range(len(list_of_countries)):
        list_of_countries[i] = list_of_countries[i]['name']
    # concatenate all the countries to one string
    country_production = ''
    count = 0
    for i in range(len(list_of_countries)):
        country_production += list_of_countries[i]
        if (i != len(list_of_countries) - 1):
            country_production += ','
    if country_production == '':
        country_production = None
    return country_production


def get_director(id):
    info_director = requests.get('https://api.themoviedb.org/3/movie/' + str(
        id) + '?api_key=' + TMDB_KEY + '&language=uk-UA&append_to_response=credits')
    crew = info_director.json()['credits']['crew']
    director = ''
    for element in crew:
        if (element['job'] == 'Director'):
            director = element['name']
            break
        else:
            director = ' '
    return director


def get_local_studios():
    request_local_studios = requests.get('https://ekinoback.herokuapp.com/studios')
    local_studios = []
    for studio in request_local_studios.json():
        local_studios.append(studio['name'])
    return local_studios


def get_studios(film_object):
    # list for companies
    all_companies = []
    # get all the companies
    list_of_companies = film_object['production_companies']

    local_companies = get_local_studios()

    # take only 5 studios

    for count,company in enumerate(list_of_companies):
        if(count == 5):
            break
        if (company['name'] not in local_companies):
            pass
            r = requests.post('https://ekinoback.herokuapp.com/studios', json={"name": company['name']})

        all_companies.append(company['name'])
    return all_companies


def get_description(film_object):
    description = ''
    if (film_object['overview'] == ''):
        description = None
    else:
        description = film_object['overview']
    return description


def get_film(movie_id):
    film = requests.get('https://api.themoviedb.org/3/movie/' + str(
        movie_id) + '?api_key=' + TMDB_KEY + '&language=uk-UA')

    film = film.json()

    loc_dict = {}

    # title
    loc_dict['name'] = get_title(film)

    # trailer_link
    loc_dict['trailer_link'] = get_trailer(film, movie_id)

    # poster url
    loc_dict['poster_link'] = get_poster(film)

    # genres
    loc_dict['genre'] = get_genres(film)

    # if age_limit True: 18+
    loc_dict['age'] = get_AgeLimit(film)

    # id for imdb api
    loc_dict['imdb_id'] = get_imdbId(film)

    # rating
    loc_dict['rating'] = get_rating(film)

    # duration of film
    loc_dict['duration'] = get_duration(film)

    # release date
    loc_dict['release_date'] = get_ReleaseDate(film)

    # actors
    loc_dict['actors'] = get_actors(movie_id)

    # country production
    loc_dict['country_production'] = get_country_production(film)

    # director
    loc_dict['director'] = get_director(movie_id)

    # studio
    loc_dict['studio'] = get_studios(film)

    # description
    loc_dict['description'] = get_description(film)

    return loc_dict

def update_films(url):
    # amount of pages
    nums_of_pages = get_pages(url)

    for page in range(1, nums_of_pages + 1):

        # list of film's id
        films_id = get_IDlist(page,url)

        # get every film by theirs id
        for movie_id in films_id:
            film_dict = get_film(movie_id)
            print(film_dict)

            r = requests.post('https://ekinoback.herokuapp.com/movies', json=film_dict)
            print(r)


update_films(UPCOMING)
update_films(NOW_PLAYING)

finish = perf_counter()
print(finish - start)
