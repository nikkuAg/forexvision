from forex_backend.models import ExchangeRate
from rest_framework.serializers import ModelSerializer


class ExchangeRateSerializer(ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = "__all__"
