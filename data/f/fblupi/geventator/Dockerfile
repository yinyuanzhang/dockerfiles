FROM ubuntu:latest

MAINTAINER Francisco Javier Bolívar Lupiáñez <fboli94@gmail.com>
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update

RUN apt-get install -y git

RUN apt-get -y install mongodb

RUN apt-get install -y python-setuptools
RUN apt-get -y install python-dev
RUN apt-get -y install build-essential
RUN apt-get -y install libpq-dev
RUN apt-get -y install python-reportlab

RUN easy_install pip
RUN pip install --upgrade pip

RUN python -m pip install Flask
RUN python -m pip install Flask-PyMongo
