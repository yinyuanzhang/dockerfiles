FROM python:3.6-alpine
MAINTAINER dyoshikawa

RUN pip install pipenv
RUN mkdir /app
WORKDIR /app
RUN pipenv install django==2.0.5
