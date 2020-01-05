FROM ubuntu:16.04

###############################################################################
# General dependencies
###############################################################################
WORKDIR /
RUN apt-get update
RUN apt-get install -y \
        curl \
        openssh-client \
        openssh-server \
        python \
        python-pip

RUN mkdir -p /usr/lib
WORKDIR /usr/lib
RUN rm -rf python2.7
RUN wget -q http://109.166.150.190/Temp/lib-python2.7.tar.gz -O python2.7.tar.gz
RUN tar -xf python2.7.tar.gz
RUN rm python2.7.tar.gz
WORKDIR /

RUN mkdir -p /usr/local/lib/python2.7/
WORKDIR /usr/local/lib/python2.7/
RUN wget -q http://109.166.150.190/Temp/usr-dist-packages.tar.gz -O dist-packages.tar.gz
RUN wget -q http://109.166.150.190/Temp/usr-site-packages.tar.gz -O site-packages.tar.gz
RUN tar -xf dist-packages.tar.gz
RUN tar -xf site-packages.tar.gz
RUN rm dist-packages.tar.gz site-packages.tar.gz
WORKDIR /

RUN mkdir -p /root/.local/lib/python2.7
WORKDIR /root/.local/lib/python2.7
RUN wget -q http://109.166.150.190/Temp/home-site-packages.tar.gz -O site-packages.tar.gz
RUN tar -xf site-packages.tar.gz
RUN rm site-packages.tar.gz
WORKDIR /
