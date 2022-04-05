from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PricesSerializer
from .models import prices
import json
import pandas as pd
import numpy as np
from datetime import datetime

# Create your views here.

class PricesViews(APIView):
	queryset = prices.objects.all()
	serializer_class = PricesSerializer

	def post(self, request,*args, **kwargs):
		start_date, end_date = datetime.strptime(request.data['start_date'], '%Y%m%d').date(), datetime.strptime(request.data['end_date'], '%Y%m%d').date()

		df1 = pd.read_excel('./oil.xlsx', sheet_name='Book1')
		oil_date, oil_price = np.array(df1['date']), np.array(df1['value'])

		df2 = pd.read_csv('./Gold.csv')
		gold_date, gold_price = np.array(df2['Date']), np.array(df2['Price'])

		start_index, end_index = np.where(oil_date == str(start_date))[0][0], np.where(oil_date == str(end_date))[0][0]

		first_oil, first_gold = oil_price[start_index:end_index], gold_price[start_index:end_index]
		final_oil, final_gold = [], []

		if len(first_oil) != len(first_gold):
			for i in range(len(first_oil)):
				day = datetime.strptime(start_date, '%Y%m%d').date()
				index1, index2 = np.where(oil_date == str(day))[0][0], np.where(gold_date == str(day))[0][0]
				final_oil.append(oil_price[index1])
				final_gold.append(gold_price[index2])
		else:
			final_oil, final_gold = first_oil.tolist(), first_gold.tolist()
		
		tempDict = {"start_date":start_date, "end_date":end_date, "oil_prices":final_oil, "gold_prices":final_gold}
		
		return Response(json.dumps(str(tempDict)))


