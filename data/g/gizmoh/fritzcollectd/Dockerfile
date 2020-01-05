FROM camptocamp/collectd:latest

MAINTAINER René Wißkirchen <rene.wisskirchen@gmail.com>

RUN apt-get update \
 && apt-get -y upgrade \
 && apt-get install -y apt-utils libvarnishapi1 python-pip libxml2-dev libxslt1-dev\
 build-essential libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev zlib1g zlib1g-dev wget libpython-dev
RUN wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
RUN tar -xzvf Python-3.7.0.tgz
WORKDIR Python-3.7.0
RUN ./configure --enable-optimizations
RUN make
RUN make install

RUN apt-get update \
 && apt-get -y upgrade python3-setuptools python-setuptools
RUN pip install --upgrade pip
RUN pip install fritzcollectd

RUN apt-get clean \
 && rm -rf /var/lib/apt/lists/*
