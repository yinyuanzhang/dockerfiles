FROM ubuntu:14.04.1

MAINTAINER Mike Chelen <michael.chelen@gmail.com>

RUN apt-get -y update && apt-get install -y \
  erlang \
  git \
  python-pip \
  python-dev \
  libevent-dev \
  couchdb \
  libjpeg-dev \
  zlib1g-dev \
  libpng12-dev \
  libpq-dev \
  python-virtualenv


  
RUN git clone git://github.com/gpodder/mygpo.git

RUN cd mygpo 

RUN virtualenv env

RUN ./env/bin/pip install -r requirements.txt



  
  
  
