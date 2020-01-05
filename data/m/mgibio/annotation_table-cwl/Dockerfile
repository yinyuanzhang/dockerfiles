FROM ubuntu:xenial
MAINTAINER John Garza <johnegarza@wustl.edu>

LABEL \
    description="Image supporting a helper python script"

#libcurl4, libssl, zlib1g are necessary for pip to install cyvcf2
RUN apt-get update -y && apt-get install -y \
python \
python-pip \
libcurl4-openssl-dev \
libssl-dev \
zlib1g-dev

RUN pip install --upgrade pip

RUN pip install cyvcf2==0.10.1

COPY add_annotations_to_table_helper.py /usr/bin/add_annotations_to_table_helper.py
