from forex_backend.models import ExchangeRate
from forex_backend.serializer import ExchangeRateSerializer
from forex_backend.utils import (convert_period_to_date_range,
                                 validate_date_range, validate_quote)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ForexView(APIView):
    def post(self, request, *args, **kwargs):
        period = request.data.get("period", None)
        start_date = request.data.get("start_date", None)
        end_date = request.data.get("end_date", None)
        quote = request.data.get("quote", None)

        try:
            quote = validate_quote(quote)
            if period:
                start_date, end_date = convert_period_to_date_range(period)
            else:
                start_date, end_date = validate_date_range(start_date, end_date)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        data = ExchangeRate.objects.filter(
            date__range=(start_date, end_date), quote=quote
        )

        data = ExchangeRateSerializer(data, many=True).data

        return Response(data, status=status.HTTP_200_OK)
