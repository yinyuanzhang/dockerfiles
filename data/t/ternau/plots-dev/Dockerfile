FROM python:3-alpine

WORKDIR /home

RUN apk add wget git

# Git release tag
ARG release=0.6.2

RUN wget https://bitbucket.org/terndatateam/eco-portal-prototype/get/$release.tar.gz

RUN mkdir app
RUN tar xzf $release.tar.gz -C app --strip 1

WORKDIR /home/app

RUN pip3 install --upgrade pip --no-cache-dir
RUN pip3 install -r requirements.txt --no-cache-dir

RUN wget http://linkeddata.tern.org.au/viewer/corveg/download
RUN mv download CORVEG.ttl

RUN apk add --no-cache elasticsearch

EXPOSE 8000

CMD gunicorn -b 0.0.0.0:8000 --workers=3 --threads=3 portal:app
