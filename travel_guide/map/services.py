# services/services.py

import requests


# def get_coordinates(place_name):
#     api_key = '4f01ebd046984b8da794ce2ecd74a2ba'
#     base_url = f'https://api.opencagedata.com/geocode/v1/json?q={place_name}'
#     params = {
#         'key': api_key,
#     }

#     response = requests.get(base_url, params=params)
#     data = response.json()
#     print(data)
#     if response.status_code == 200:
#         return data
#     else:
#         return None

def get_coordinates(place_name):
    # your actual API key for https://locationiq.com/
    api_key = 'pk.f89febc4b2a6558c5b59086b284b2605'
    base_url = f'https://us1.locationiq.com/v1/search?q={place_name}&format=json'
    params = {

        'key': api_key,
    }

    response = requests.get(base_url,params=params)
    data = response.json()

    location = data[0]
    if response.status_code == 200:
        location=data[-1]
        return location['lat'], location['lon']
    else:
        return None

def get_emergency_services(lat, lng):
    # your actual API key for https://locationiq.com/
    api_key = 'pk.f89febc4b2a6558c5b59086b284b2605'
    base_url = "https://us1.locationiq.com/v1/nearby"
    params = {
        'key': api_key,
        'lat': lat,
        'lon': lng,
        'tag': 'amenity:police,hospital',
        'radius': 3000,
        'format': 'json'
    }

    response = requests.get(base_url,params=params)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        return None