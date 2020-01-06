FROM python:3.7-slim-stretch
LABEL maintainer="PDOK dev <pdok@kadaster.nl>"

RUN apt-get -y update \
    && apt-get install -y \
               python-pil \
               python-yaml \
               libproj12 \
               libgeos-c1v5 \
               python-lxml \
               libgdal20  \
               python-shapely \
               python-pip \
               git \
    && rm -rf /var/lib/apt/lists/* 

RUN pip install PyYAML boto3 Pillow requests Shapely eventlet gunicorn
RUN pip install git+git://github.com/mapproxy/mapproxy.git

EXPOSE 80