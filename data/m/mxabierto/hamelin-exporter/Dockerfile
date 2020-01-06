FROM ubuntu:17.10

WORKDIR /hamelin-exporter

# update container
RUN apt-get clean && apt-get update && apt-get install -y locales

# SET UTF-8 AS default encoding in the container
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV PYTHONIOENCODING=UTF-8

# env setup
RUN apt-get install -y \
  git \
  python3-pip \
  python3-gdal \
  curl

# python 3 dependencies
RUN pip3 install \
  lxml \
  pandas \
  psycopg2 psycopg2-binary \
  kml2geojson \
  pymongo \
  requests \
  xlrd \
  unidecode

# clone repo
RUN git clone https://github.com/mxabierto/hamelin-exporter . && git checkout dgm
