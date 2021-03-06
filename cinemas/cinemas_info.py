import requests
from const import CINEMA_DETAILS_REQUEST, EK_CINEMAS_API


# Func return dictionary with cinema info
# @param: request_type - for which type request (POST/PUT) need info
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
        return [{
            "name": request_result.json()['result']['name'],
            "address": request_result.json()['result']['formatted_address'],
            "rating": request_result.json()['result']['rating'],
            "place_id": request_result.json()['result']['place_id'],
            "longitude": request_result.json()['result']['geometry']['location']['lng'],
            "latitude": request_result.json()['result']['geometry']['location']['lat'],
            "website_link": request_result.json()['result']['website'],
            "phone": request_result.json()['result']['formatted_phone_number']
        }]
    else:
        print('Wrong type')


# Func refresh cinema info
# @param: place_ids - unique cinema keys list
def update_cinemas_info(place_ids):
    for place_id in place_ids:
        cinema_request = EK_CINEMAS_API + '/' + place_id
        cinema = requests.get(cinema_request)

        # Check if cinema exist in our db
        # If exist (status_code == 200), than refresh (PUT)
        # If not exist, add new cinema (POST)
        if cinema.status_code == 200:
            put = requests.put(cinema_request, data=get_cinema_info(request_type='PUT', place_id=place_id))
            print(cinema.json()['name'] + ': Cinema Info PUT request:', put.status_code, put.json())
        else:
            post = requests.post(EK_CINEMAS_API, json=get_cinema_info(request_type='POST', place_id=place_id))
            print('Cinema info POST request:', post.status_code, post.json())
    print()
