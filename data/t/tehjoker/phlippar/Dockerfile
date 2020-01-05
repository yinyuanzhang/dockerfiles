FROM python:3
MAINTAINER Alan AK Kavanagh <alankavanagh1337@gmail.com>

ENV PYTHONUNBUFFERED 1

RUN mkdir /config
WORKDIR /config
ADD config/requirements.txt /config/
RUN python3.6 -m pip install -r requirements.txt

RUN mkdir /webapp
WORKDIR /webapp
ADD manage.py /webapp/
ADD phlippar_webapp /webapp/