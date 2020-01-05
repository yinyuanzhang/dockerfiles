FROM ubuntu:14.04
MAINTAINER Myles Gray "mg@mylesgray.com"

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    python-dev \
    python-pip \
    python-pycurl \
    python-software-properties \
    sudo \
    vim

EXPOSE 80 443
VOLUME ["/opt"]