from django.urls import path , include
from .views import PricesViews

urlpatterns = [
    path('prices/', PricesViews.as_view())
]