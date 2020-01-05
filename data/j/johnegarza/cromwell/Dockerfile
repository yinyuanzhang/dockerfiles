FROM ubuntu:xenial
MAINTAINER John Garza <johnegarza@wustl.edu>

LABEL \
    description="Packages necessary to run cromwell on LSF, and a few utility tools"

RUN apt-get update -y && apt-get install -y \
    apt-utils \
    default-jdk \
    curl \
    git \
    libnss-sss \
    python-pip \
    vim

RUN pip install --upgrade pip
RUN pip install pyyaml
RUN pip install unidecode
RUN pip install 'setuptools>=18.5'
RUN pip install cwltool
RUN pip install 'ruamel.yaml==0.14.2'
