FROM ubuntu:14.04
MAINTAINER Gian Burga <franco.burga@gmail.com>

ENV DATABASE_URL **NULL**
ENV SECRET_KEY **NULL**

RUN mkdir /app
WORKDIR /app
RUN apt-get update && apt-get install -y libmysqld-dev python-dev python-setuptools && easy_install pip
RUN pip install --upgrade pip
EXPOSE 8000
CMD pip install -r requirements.txt && python manage.py runserver 0.0.0.0:8000