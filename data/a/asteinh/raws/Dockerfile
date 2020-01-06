FROM python:3.7.4-buster

RUN apt-get update \
  && apt-get install -y \
    libgeos-3.* libgeos-dev \
    lftp\
    hugo

RUN pip3 install --upgrade pip
RUN pip3 install matplotlib
RUN pip3 install geonamescache
RUN pip3 install https://github.com/matplotlib/basemap/archive/master.zip
RUN pip3 install requests
RUN pip3 install pathlib
