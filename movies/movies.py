from time import perf_counter

start = perf_counter()

from modules.keysAPI import *
import requests

# global_list= []
dictionary = {}
# id of film
# id =0

# path_before poster
path_before = 'http://image.tmdb.org/t/p/w600_and_h900_bestv2'


'''

omdb.set_default('apikey', API_KEY)


var =omdb.get(title='Sonic the Hedgehog')
print(var)
# print(var['year'])
# response1 = requests.get('http://www.omdbapi.com/?t=Wonder%20Woman%201984&apikey=66fffc24')
# response2 = requests.get('http://www.omdbapi.com/?s=Wonder%20Woman%201984&apikey=66fffc24')
# print(response1.json())
# print(response2.json())

# response = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=66fffc24')
# print(response.json())
# all = requests.get("http://www.omdbapi.com/?s=inception&apikey=66fffc24")
# print(all.json())


# pag = requests.get('http://www.omdbapi.com/?page&apikey=66fffc24')
# print(pag.json())

#
print()

'''

pageuk = requests.get(
    'https://api.themoviedb.org/3/movie/now_playing?api_key=' + TMDB_KEY + '&language=uk-UA&page=1&region=UA')

# transform request to json format
pageuk = pageuk.json()

# amount of pages
nums_of_pages = pageuk['total_pages']

kilkist_filmiv = 0
for i in range(1, nums_of_pages + 1):

    pageuk = requests.get(
        'https://api.themoviedb.org/3/movie/now_playing?api_key=' + TMDB_KEY + '&language=uk-UA&page=' + str(
            i) + '&region=UA')
    pageuk = pageuk.json()
    # pages
    res = ((pageuk['results']))

    # list of id from db
    films_id = []
    for film_id in res:
        films_id.append(film_id['id'])

    # get every film by theirs id
    for movie_id in films_id:
        film = requests.get('https://api.themoviedb.org/3/movie/' + str(
            movie_id) + '?api_key=' + TMDB_KEY + '&language=uk-UA')

        film = film.json()

        loc_dict = {}

        # title
        loc_dict['name'] = film['title']

        # trailer_link link
        trailers_response = requests.get('https://api.themoviedb.org/3/movie/' + str(
            movie_id) + '/videos?api_key=' + TMDB_KEY + '&language=uk-UA')
        trailers = trailers_response.json()['results']
        try:
            trailer = 'https://www.youtube.com/watch?v=' + trailers[len(trailers) - 1]['key']
        except:
            trailer = 'https://www.google.com'
        loc_dict['trailer_link'] = trailer

        # poster url
        loc_dict['poster_link'] = path_before + film['poster_path']

        list_of_genres = film['genres']
        # list of genres
        genres = []
        for gan in list_of_genres:
            genres.append(gan['name'])
        # genres
        loc_dict['genre'] = genres

        # if age_limit True: 18+
        loc_dict['age'] = film['adult']

        # id for imdb api
        loc_dict['imdb_id'] = film['imdb_id']

        # ------
        # rating
        list_of_ratings = requests.get('http://www.omdbapi.com/?i=' + film['imdb_id'] + '&apikey=' + OMDB_KEY).json()[
            'Ratings']
        rating = ''
        for rat in list_of_ratings:
            rating += rat['Source'] + ' ' + rat['Value'] + ' '
        # rating = requests.get()
        loc_dict['rating'] = rating

        # duration of film
        loc_dict['duration'] = int(film['runtime'])

        # release date
        loc_dict['release_date'] = film['release_date']

        # actors
        actors = []
        # request for info about
        act = requests.get('https://api.themoviedb.org/3/movie/' + str(
            movie_id) + '/credits?api_key=' + TMDB_KEY + '&language=uk-UA')
        list_actors_info = act.json()['cast']
        for element in list_actors_info:
            loc_dict_actors = {}
            loc_dict_actors['character'] = element['character']
            loc_dict_actors['name'] = element['name']
            # check for empty path
            try:
                loc_dict_actors['image'] = path_before + element['profile_path']
            except:
                loc_dict_actors['image'] = ' '
            actors.append(loc_dict_actors)
        # must be this  # loc_dict['actors'] = actors
        loc_dict['actors'] = []

        # origin title
        # loc_dict['original_title'] = film['original_title']

        # country production
        # find all countries, and pass them to the list
        list_of_countries = film['production_countries']
        for i in range(len(list_of_countries)):
            list_of_countries[i] = list_of_countries[i]['name']

        # concatenate all the countries to one string
        country_production = ''
        count = 0
        for i in range(len(list_of_countries)):
            country_production += list_of_countries[i]
            if (i != len(list_of_countries) - 1):
                country_production += ','
        loc_dict['country_production'] = country_production

        # director
        info_director = requests.get('https://api.themoviedb.org/3/movie/' + str(
            movie_id) + '?api_key=' + TMDB_KEY + '&language=uk-UA&append_to_response=credits')
        crew = info_director.json()['credits']['crew']
        director = ''
        for element in crew:
            if (element['job'] == 'Director'):
                director = element['name']
                break
            else:
                director = ' '

        # /director = ''
        loc_dict['director'] = director

        # list for companies
        all_companies = []
        # get all the companies
        list_of_companies = film['production_companies']
        for company in list_of_companies:
            all_companies.append(company['name'])

        # add the list to the dictionary
        # must be this # loc_dict['studio'] = all_companies
        loc_dict['studio'] = []

        # description
        if (film['overview'] == ''):
            loc_dict['description'] = ' - '
        else:
            loc_dict['description'] = film['overview']

        # status if the film was released
        # loc_dict['status']= film['status']

        print(loc_dict)
        r = requests.post('http://127.0.0.1:8000/movies/', json=loc_dict)
        print(r)
        break

        kilkist_filmiv += 1

        # dictionary[id] = loc_dict

        # id+=1

finish = perf_counter()
print(finish - start)
print(kilkist_filmiv)

# with open('films.json', 'w', encoding='utf-8') as json_file:
#     json.dump(dictionary, json_file)

# pages = omdb.get(page = )
# print(pages)


'''
{
"name": "Бладшот4345",
"trailer_link": "https://www.youtube.com/watch?v=pWbL7f0RBFY",
"poster_link": "http://image.tmdb.org/t/p/w600_and_h900_bestv2/fw5qiCNYdCYiPlB2xJvLEnugZNa.jpg",
"genre" :["Бойовик", "Фантастика"],
 "age" : "True",
 "rating" : 4.2,
 "duration" : 100,
 "release_date" : "2020-03-05",
 "actors" : [],
 "country_production" : "China,United States of America",
 "director" : "me",
 "studio" : [],
 "description": "agagga"
}'''

'''
# {'name': 'Бладшот', 'trailer_link': 'https://www.youtube.com/watch?v=pWbL7f0RBFY', 'poster_link': 'http://image.tmdb.org/t/p/w600_and_h900_bestv2/fw5qiCNYdCYiPlB2xJvLEnugZNa.jpg', 'genre': ['Бойовик', 'Фантастика'], 'age': False, 'rating': 4.2, 'duration': 110, 'release_date': '2020-03-05', 'actors': [], 'country_production': 'China,United States of America', 'director': 'Dave Wilson', 'studio': [], 'description': 'Секретна корпорація RST повертає до життя смертельно пораненого морпіха Рея Ґаррісона. Завдяки нанотехнологіям він стає Бладшотом – невразливою біотехнологічною зброєю, універсальним солдатом з надлюдською силою. Контролюючи тіло Рея, компанія керує його розумом і спогадами. Бладшот не знає, хто він насправді, і його завдання це з’ясувати.'}
'''
