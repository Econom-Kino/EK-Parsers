<<<<<<< HEAD
from keys import GOOGLE_API_KEY,TMDB_KEY
=======
from keys import GOOGLE_API_KEY, TMDB_KEY
>>>>>>> ce66c225d2aec10ce36976b7440bf62747a087d6


# Cinemas
# EK_CINEMAS_API = 'https://ekinoback.herokuapp.com/cinemas/'
EK_CINEMAS_API = 'http://127.0.0.1:8000/cinemas/'
CINEMA_DETAILS_API = 'https://maps.googleapis.com/maps/api/place/details/json?language=uk&'
CINEMA_DETAILS_FIELDS = 'name,rating,formatted_phone_number,place_id,website,formatted_address,geometry'
CINEMA_DETAILS_REQUEST = CINEMA_DETAILS_API + 'fields=' + CINEMA_DETAILS_FIELDS + '&key=' + GOOGLE_API_KEY

# Cinema photos
# EK_CINEMA_IMAGES_API = 'https://ekinoback.herokuapp.com/cinema-images/'
EK_CINEMA_IMAGES_API = 'http://127.0.0.1:8000/cinema-images/'
CINEMA_PHOTOS_API = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1000&photoreference='

<<<<<<< HEAD

# films
NOW_PLAYING = 'https://api.themoviedb.org/3/movie/now_playing?api_key=' + TMDB_KEY + '&language=uk-UA&region=UA'
UPCOMING = 'https://api.themoviedb.org/3/movie/upcoming?api_key=' + TMDB_KEY + '&language=uk-UA&region=UA'
=======
# Genres
EK_GENRES_API = 'https://ekinoback.herokuapp.com/genres/'
# EK_GENRES_API = 'http://127.0.0.1:8000/genres/'
GENRES_API = 'https://api.themoviedb.org/3/genre/movie/list?'
GENRES_REQUEST = GENRES_API + 'language=uk-UA&api_key=' + TMDB_KEY
>>>>>>> ce66c225d2aec10ce36976b7440bf62747a087d6
