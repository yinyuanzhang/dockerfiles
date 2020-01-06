############################################################
# Dockerfile to build uwsgi using python3 container images
# Based on Ubuntu 16.04
############################################################

FROM ubuntu:16.04
MAINTAINER ngocluanbka

RUN apt-get update && \
    apt-get install -y python3-pip && \
    apt-get autoclean && \
    apt-get clean && \
    apt-get autoremove

# update pip
RUN pip3 install -U pip setuptools uwsgi 

# # install uwsgi
# RUN pip3 install uwsgi

# INSTALL requirements before for caching
COPY app /app
COPY requirements.txt /requirements.txt
COPY uwsgi_config.ini /uwsgi_config.ini
# install requirements
RUN pip3 install -r requirements.txt

# APPLICATION
VOLUME ["/app"]

# expose ports
EXPOSE 5000

CMD uwsgi --ini /uwsgi_config.ini
