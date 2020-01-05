FROM ubuntu:xenial

MAINTAINER eyalrounds

RUN DEBIAN_FRONTEND=noninteractive apt-get -yqq update \
 && DEBIAN_FRONTEND=noninteractive apt-get -yqq install  texinfo libglib2.0-dev autoconf \
	libtool libsdl-dev build-essential golang git curl unzip python-pip python\
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip install --upgrade pip
RUN pip install numpy scipy pandas matplotlib seaborn graphviz scikit-learn
