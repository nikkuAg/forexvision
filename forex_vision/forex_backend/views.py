from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from forex_backend.models import ExchangeRate
from forex_backend.serializer import ExchangeRateSerializer
from forex_backend.utils import (convert_period_to_date_range,
                                 validate_date_range, validate_quote)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ForexView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["quote"],
            properties={
                "quote": openapi.Schema(type=openapi.TYPE_STRING, description="Quote"),
                "period": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Period"
                ),
                "start_date": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Start date"
                ),
                "end_date": openapi.Schema(
                    type=openapi.TYPE_STRING, description="End date"
                ),
            },
            example={
                "quote": "EURUSD",
                "period": "1M",
            },
        ),
        responses={
            200: openapi.Response("Success"),
            400: openapi.Response("Bad Request"),
        },
    )
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
