FROM python:3.6.8-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN mkdir django_discovery

# RUN  django-admin startproject django_discovery
# WORKDIR /usr/src/app/django_discovery

# CMD [ "python", "/usr/src/app/start_django.py" ]
