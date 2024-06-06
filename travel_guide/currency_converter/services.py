# services/services.py

import requests

class CurrencyConverter:
    def __init__(self):
        # your actual API key for https://www.exchangerate-api.com/
        self.api_key = 'ce5c7b1db80873b2748effa9'
        self.base_url = 'https://v6.exchangerate-api.com/v6/'


    def get_currency_codes(self):
        url = f'https://v6.exchangerate-api.com/v6/{self.api_key}/codes'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return dict(data['supported_codes'])
        else:
            return[]

    def get_exchange_rate(self, from_currency, to_currency):
        url = f'{self.base_url}{self.api_key}/latest/{from_currency}'
        params = {'api_key': self.api_key, 'base': from_currency}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data['conversion_rates'].get(to_currency)
        else:
            return None

    def convert_currency(self, amount, from_currency, to_currency):
        exchange_rate = self.get_exchange_rate(from_currency, to_currency)
        if exchange_rate is not None:
            converted_amount = float(amount) * float(exchange_rate)
            return converted_amount
        return None

