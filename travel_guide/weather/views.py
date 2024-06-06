from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
import requests

class WeatherAPIView(APIView):
    def get(self, request, cityname):
        api_key = '081b52fcf5a145fe3e9f58636200882c'

        url = f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
            temperature_kelvin = weather_data['main']['temp']
            temperature_celsius = round(temperature_kelvin - 273.15)
            
            
            serializer = WeatherSerializer(data={
                'city': cityname,
                'temperature': temperature_celsius,
                'humidity': weather_data['main']['humidity'],
                'description': weather_data['weather'][0]['description']
            })

            if serializer.is_valid():
                return Response(serializer.validated_data)
            else:
                return Response(serializer.errors, status=400)
        else:
            if response.status_code == 404:
                return Response({'message': 'Weather data not found'}, status=404)
            else:
                return Response({'message': 'Failed to retrieve weather data'}, status=response.status_code)
            