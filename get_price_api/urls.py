from django.urls import path , include
from .views import PricesViews#, UserCreate
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('prices/', PricesViews.as_view()),
    path('token/', obtain_auth_token, name='api_token_auth'),
    # path('register/', UserCreate.as_view()),
]
