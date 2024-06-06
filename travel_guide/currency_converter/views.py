from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import CurrencyConverter
from .serializers import CurrencyConversionSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class CurrencyConversionView(APIView):
    serializer_class = CurrencyConversionSerializer
    permission_classes = [AllowAny]

    def get(self,request):
        currency_converter = CurrencyConverter()
        currency_codes = currency_converter.get_currency_codes()
        if currency_codes is not None:
            response_data = {'currency_codes': currency_codes}
            return Response(response_data)
        else:
            return Response({'error': 'Unable to fetch information'},status=500)

    def post(self, request):
        serializer = CurrencyConversionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        amount = serializer.validated_data['amount']
        from_currency = serializer.validated_data['from_currency']
        to_currency = serializer.validated_data['to_currency']

        # Make sure to replace 'your_api_key' with your actual API key
        currency_converter = CurrencyConverter()

        converted_amount = currency_converter.convert_currency(amount, from_currency, to_currency)

        if converted_amount is not None:
            response_data = {'converted_amount': converted_amount}
            return Response(response_data)
        else:
            return Response({'error': 'Unable to fetch exchange rates'}, status=500)



