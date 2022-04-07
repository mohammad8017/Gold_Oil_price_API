from traceback import print_tb
from turtle import fd, st
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PricesSerializer
from .models import prices
import json
import pandas as pd
import numpy as np
from datetime import datetime
import requests as req
from persiantools.jdatetime import JalaliDate
from datetime import timedelta 

# Create your views here.

class PricesViews(APIView):
	queryset = prices.objects.all()
	serializer_class = PricesSerializer

	def post(self, request,*args, **kwargs):
		start_date, end_date = str(datetime.strptime(request.data['start_date'], '%Y%m%d').date()), str(datetime.strptime(request.data['end_date'], '%Y%m%d').date())

		data = req.get('http://tsetmc.ir/tsev2/chart/data/Index.aspx?i=32097828799138957&t=value').text.split(';')
		shakhes, shakhes_date = [], []

		for date in data:
			splitted = date.split(',')
			day = list(map(int, splitted[0].split('/')))
			miladi_date = JalaliDate(day[0], day[1], day[2]).to_gregorian()
			shakhes.append(float(splitted[1]))
			shakhes_date.append(miladi_date)

		df1 = pd.read_excel('./oil.xlsx', sheet_name='Book1')
		oil_date, oil_price = np.array(df1['date']), np.array(df1['value'])

		df2 = pd.read_csv('./Gold.csv')
		gold_date, gold_price = np.array(df2['Date']), np.array(df2['Price'])

		final_oil, final_gold, final_shakhes = [], [], []

		sday = datetime.strptime(start_date, '%Y-%m-%d').date()
		fday = datetime.strptime(end_date, '%Y-%m-%d').date()
		days_count = (fday-sday).days
		for i in range(days_count):
			currDate = sday + timedelta(days=i)
			try:
				index1, index2 = np.where(oil_date == str(currDate))[0][0], np.where(gold_date == str(currDate))[0][0]
				index3 = shakhes_date.index(currDate)
				final_shakhes.append(shakhes[index3])
				final_oil.append(oil_price[index1])
				final_gold.append(gold_price[index2])
			except:
				continue

		
		tempDict = {"start_date":start_date, "end_date":end_date, "oil_prices":final_oil, "gold_prices":final_gold, "shakhes":final_shakhes}
		
		return Response(json.dumps(str(tempDict)))


