# services/services.py

import requests


class Countrycode_Service:
    def __init__(self):
        self.base_url = 'https://www.travel-advisory.info/api'

    def iso_countrycode(self):
        url = f'{self.base_url}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            codes=dict(map(lambda v: (v['name'],v['iso_alpha2']),data['data'].values()))
            return codes
        else:
            return None

class SafetyService:
    def __init__(self):
        self.base_url = 'https://www.travel-advisory.info/api'

    def get_safety_information(self, country_code=None):
        if country_code:
            url = f'{self.base_url}?countrycode={country_code}/'
        else:
            url = f'{self.base_url}'

        response = requests.get(url)

        if response.status_code == 200:        
            data = response.json()
                
            return data['data']
        else:
            return None


