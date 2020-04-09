import requests
from const import CINEMA_DETAILS_REQUEST, EK_CINEMAS_API


# Функція сформаваний словник інформацією про кінотеатр
# @param: request_type - вказує для якого запиту (POST/PUT) протрібна інформація
def get_cinema_info(request_type, place_id):
    get_details_request = CINEMA_DETAILS_REQUEST + '&place_id=' + place_id
    request_result = requests.get(get_details_request)

    if request_type == 'PUT':
        return {
            "name": request_result.json()['result']['name'],
            "address": request_result.json()['result']['formatted_address'],
            "rating": request_result.json()['result']['rating'],
            "place_id": request_result.json()['result']['place_id'],
            "longitude": request_result.json()['result']['geometry']['location']['lng'],
            "latitude": request_result.json()['result']['geometry']['location']['lat'],
            "website_link": request_result.json()['result']['website']
        }
    elif request_type == 'POST':
        return {
            "name": request_result.json()['result']['name'],
            "address": request_result.json()['result']['formatted_address'],
            "rating": request_result.json()['result']['rating'],
            "place_id": request_result.json()['result']['place_id'],
            "longitude": request_result.json()['result']['geometry']['location']['lng'],
            "latitude": request_result.json()['result']['geometry']['location']['lat'],
            "website_link": request_result.json()['result']['website'],
            "phone": request_result.json()['result']['formatted_phone_number']
        }
    else:
        print('Wrong type')


# Функція оновлює інфу кінотеатрів
# @param: place_ids - список кінотеатрів
def update_cinemas_info(place_ids):
    for place_id in place_ids:
        cinema_request = EK_CINEMAS_API + 'place_id/' + place_id + '/'
        cinema = requests.get(cinema_request)

        # Перавіряю чи є кінотеатр в базі
        # Якщо є (status_code == 200), то оновлюю інформацію (PUT)
        # Якщо немає (status_code == 404), то додаю новий кінотеатр (POST)
        if cinema.status_code == 200:
            put = requests.put(cinema_request, data=get_cinema_info(request_type='PUT', place_id=place_id))
            print(cinema.json()['name'] + ': Cinema Info PUT request:', put.status_code)
        elif cinema.status_code == 404:
            post = requests.post(EK_CINEMAS_API, data=get_cinema_info(request_type='POST', place_id=place_id))
            print('Cinema info POST request:', post.status_code)
        else:
            print("update_cinemas_info: Something goes ne tak")
    print()
