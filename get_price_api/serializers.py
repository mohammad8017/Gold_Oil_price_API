from rest_framework import serializers
from django.contrib.auth.models import User
from .models import prices
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.models import User

class PricesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = prices
        fields = ('start_date', 'end_date')


