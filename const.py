from keys import GOOGLE_API_KEY, TMDB_KEY


# Cinemas
EK_CINEMAS_API = 'https://ekinoback.herokuapp.com/cinemas'
CINEMA_DETAILS_API = 'https://maps.googleapis.com/maps/api/place/details/json?language=uk&'
CINEMA_DETAILS_FIELDS = 'name,rating,formatted_phone_number,place_id,website,formatted_address,geometry'
CINEMA_DETAILS_REQUEST = CINEMA_DETAILS_API + 'fields=' + CINEMA_DETAILS_FIELDS + '&key=' + GOOGLE_API_KEY

# Cinema photos
EK_CINEMA_IMAGES_API = 'https://ekinoback.herokuapp.com/cinema-images'
CINEMA_PHOTOS_API = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1000&photoreference='

# Genres
EK_GENRES_API = 'https://ekinoback.herokuapp.com/genres'
GENRES_API = 'https://api.themoviedb.org/3/genre/movie/list?'
GENRES_REQUEST = GENRES_API + 'language=uk-UA&api_key=' + TMDB_KEY

# Sessions
EK_SESSIONS_API = 'https://ekinoback.herokuapp.com/sessions'
EK_IN_ROLLING_API = 'https://ekinoback.herokuapp.com/movies/in-rolling'
