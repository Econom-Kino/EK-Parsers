from keys import GOOGLE_API_KEY, TMDB_KEY


# Cinemas
EK_CINEMAS_API = 'https://ekinoback.herokuapp.com/cinemas'
CINEMA_DETAILS_API = 'https://maps.googleapis.com/maps/api/place/details/json?language=uk&'
CINEMA_DETAILS_FIELDS = 'name,rating,formatted_phone_number,place_id,website,formatted_address,geometry'
CINEMA_DETAILS_REQUEST = CINEMA_DETAILS_API + 'fields=' + CINEMA_DETAILS_FIELDS + '&key=' + GOOGLE_API_KEY

# Cinema photos
EK_CINEMA_IMAGES_API = 'https://ekinoback.herokuapp.com/cinema-images'
CINEMA_PHOTOS_API = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1000&photoreference='


# Films
NOW_PLAYING = 'https://api.themoviedb.org/3/movie/now_playing?api_key=' + TMDB_KEY + '&language=uk-UA&region=UA'
UPCOMING = 'https://api.themoviedb.org/3/movie/upcoming?api_key=' + TMDB_KEY + '&language=uk-UA&region=UA'


# Genres
EK_GENRES_API = 'https://ekinoback.herokuapp.com/genres'
GENRES_API = 'https://api.themoviedb.org/3/genre/movie/list?'
GENRES_REQUEST = GENRES_API + 'language=uk-UA&api_key=' + TMDB_KEY


# Sessions
EK_SESSIONS_API = 'https://ekinoback.herokuapp.com/sessions'
EK_IN_ROLLING_API = 'https://ekinoback.herokuapp.com/movies/in-rolling'
EK_CLEAR_SESSIONS = 'https://ekinoback.herokuapp.com/clear/sessions'
EK_MOVIES = 'https://ekinoback.herokuapp.com/movies'
EK_ANNOUNCES = 'https://ekinoback.herokuapp.com/movies/announces'


# Unique cinema keys list
PLACE_IDs = ["ChIJl3xz8QnnOkcReSOln9d6RqY",
             "ChIJ4dGDScndOkcRK6iYsuY5rCk",
             "ChIJif8CqgvdOkcRxDok8ta8w7Y",
             "ChIJG3CADybmOkcRkBn2_jOgbyA",
             "ChIJjW4PlXLdOkcRH4w0juRF9Ww",
             "ChIJ3X6gOm3oOkcRirf_eSmxXSI"]
