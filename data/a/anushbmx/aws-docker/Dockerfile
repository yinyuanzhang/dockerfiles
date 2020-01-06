FROM ubuntu:16.04
MAINTAINER Anush

RUN apt-get update && \
    apt-get upgrade -y

RUN apt-get install -y --no-install-recommends \
    zip \
    unzip \
    curl \
    python-pip \
    groff \
    python-setuptools
    
RUN pip install -U pip
RUN pip install awscli
