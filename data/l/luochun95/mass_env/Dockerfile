FROM centos:centos7
MAINTAINER luochun <luo_chun@massclouds.com>

ENV LANG en_US.UTF-8

WORKDIR /tmp/

RUN yum install epel-release python-setuptools -y

RUN curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python

RUN yum install gcc \
    make \
    python-devel  \
    mysql-devel \
    zeromq \
    zeromq-devel \
    bzip2-devel \
    libcurl \
    libcurl-devel \
    openssl-devel \
    libevent-devel \
    libffi-devel \
    glib2-devel \
    libjpeg-devel \
    mysql-devel \
    postgresql-devel \
    ncurses-devel \
    readline \
    readline-devel \
    sqlite-devel \
    openssl \
    openssl-devel \
    libxml2-devel \
    libxslt-devel \
    zlib-devel \
    libyaml-devel \
    wget \
    git \
    vim \
    supervisor \
    nginx \
    iotop \
    -y && yum clean all

COPY ./requirements.txt /tmp/

RUN pip install  -r requirements.txt  &&  rm -f requirements.txt 

