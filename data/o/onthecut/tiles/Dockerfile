FROM ubuntu:bionic

RUN apt-get update && \
    apt-get install -y wget tilestache && \
    mkdir -p /onthecut

WORKDIR /onthecut

ADD config.json /onthecut/config.json

RUN mkdir -p /onthecut/data && \
    wget -O data/canals.geojson https://opendata.arcgis.com/datasets/dab91c04078b4deb890c4381f4a7141a_1.geojson && \
    wget -O data/locks.geojson https://opendata.arcgis.com/datasets/69d977d61a4f4330ae0f864d0ee34cc7_0.geojson

CMD tilestache-server -c config.json -i 0.0.0.0
