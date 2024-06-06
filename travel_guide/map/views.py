from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import get_coordinates,get_emergency_services



# class EmergencyServicesView(APIView):
#     def post(self, request, *args, **kwargs):
#         place_name = request.data.get('place_name')

#         if not place_name:
#             return Response({'error': 'Place name is required'}, status=status.HTTP_400_BAD_REQUEST)

#         coordinates = get_coordinates(place_name)

#         if coordinates:
#             return Response({'coordinates': coordinates})
#         else:
#             return Response({'error': 'Failed to obtain coordinates'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmergencyServicesView(APIView):
    def post(self, request, *args, **kwargs):
        place_name = request.data.get('place_name')

        if not place_name:
            return Response({'error': 'Place name is required'}, status=status.HTTP_400_BAD_REQUEST)

        coordinates = get_coordinates(place_name)

        if not coordinates:
            return Response({'error': 'Failed to obtain coordinates'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        lat, lng = coordinates
        
        emergency_services = get_emergency_services(lat, lng)

        if not emergency_services:
            return Response({'error': 'Failed to obtain emergency services'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'emergency_services': emergency_services})