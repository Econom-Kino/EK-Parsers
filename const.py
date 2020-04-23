from keys import GOOGLE_API_KEY,TMDB_KEY


# Cinemas
EK_CINEMAS_API = 'http://127.0.0.1:8000/cinemas/'
CINEMA_DETAILS_API = 'https://maps.googleapis.com/maps/api/place/details/json?language=uk&'
CINEMA_DETAILS_FIELDS = 'name,rating,formatted_phone_number,place_id,website,formatted_address,geometry'
CINEMA_DETAILS_REQUEST = CINEMA_DETAILS_API + 'fields=' + CINEMA_DETAILS_FIELDS + '&key=' + GOOGLE_API_KEY

# Cinema photos
EK_CINEMA_IMAGES_API = 'http://127.0.0.1:8000/cinema-images/'
CINEMA_PHOTOS_API = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1000&photoreference='


# films
NOW_PLAYING = 'https://api.themoviedb.org/3/movie/now_playing?api_key=' + TMDB_KEY + '&language=uk-UA&region=UA'
UPCOMING = 'https://api.themoviedb.org/3/movie/upcoming?api_key=' + TMDB_KEY + '&language=uk-UA&region=UA'