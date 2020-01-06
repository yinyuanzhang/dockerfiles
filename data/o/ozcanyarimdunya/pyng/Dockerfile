FROM python:3.6

WORKDIR /app

RUN apt-get -qq update && apt-get -qq -y upgrade

RUN apt-get install -qq -y vim curl libpq-dev build-essential nginx

RUN rm /etc/nginx/sites-enabled/default

RUN rm /etc/nginx/sites-available/default

