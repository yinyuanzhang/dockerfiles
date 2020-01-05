FROM fulbito/fulbito-python

MAINTAINER Zeta <zetahernandez@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# remove several traces of debian python
RUN apt-get update && apt-get install -y \
        nginx && \
        rm /etc/nginx/sites-enabled/default

RUN pip install uwsgi

COPY requirements.txt /usr/src/app/

ADD startup.sh /startup.sh
ADD run_celery.sh /run_celery.sh

EXPOSE 8000

WORKDIR /usr/src/app

ADD uswgi/uwsgi.ini /uwsgi.ini

RUN pip install -r /usr/src/app/requirements.txt

