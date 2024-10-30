from django.urls import path

from .views import ForexView

urlpatterns = [path("forex-data/", ForexView.as_view())]
