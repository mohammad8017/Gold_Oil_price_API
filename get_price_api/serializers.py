from rest_framework import serializers
from .models import prices

class PricesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = prices
        fields = ('start_date', 'end_date')