FROM python:3.6.5

RUN apt-get update && apt-get -y upgrade

RUN wget https://download.osgeo.org/geos/geos-3.5.1.tar.bz2 \
    && tar xjf geos-3.5.1.tar.bz2 \
    && cd geos-3.5.1 && ./configure && make && make install
RUN rm geos-3.5.1.tar.bz2 && rm -rf geos-3.5.1

RUN apt-get install -y python3-dev libxml2-dev libxslt1-dev zlib1g-dev gdal-bin

RUN apt-get install -y postgresql-client
