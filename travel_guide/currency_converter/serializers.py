from rest_framework import serializers

class CurrencyConversionSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    from_currency = serializers.CharField(max_length=3)
    to_currency = serializers.CharField(max_length=3)


# class SafetySerializer(serializers.Serializer):
#     country_code = serializers.CharField(max_length=2)


class EmergencyServiceSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    # Add more fields as needed