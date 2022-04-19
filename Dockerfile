FROM python:latest
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY get_price_api ./get_price_api
COPY price ./price
COPY manage.py .
COPY  Gold.csv .
COPY oil.xlsx .
