FROM python:3.7

MAINTAINER Byeong0, <byeong0@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    apt-utils \
    locales \
    tzdata \
    libssl-dev \
    curl \
    vim \
    git \
    #libaio1 \
    #alien \
    default-libmysqlclient-dev \
	python-opencv && \
	rm -rf /var/lib/apt/lists/*

RUN locale-gen en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL C.UTF-8
ENV TZ=Asia/Seoul

# oracle instanctclient install
# https://oracle.github.io/odpi/doc/installation.html
#
#RUN mkdir -p /opt/oracle/
#RUN wget -q -P /opt/oracle/ http://yum.oracle.com/repo/OracleLinux/OL7/oracle/instantclient/x86_64/getPackage/oracle-instantclient19.3-basic-19.3.0.0.0-1.x86_64.rpm
#RUN alien -i /opt/oracle/oracle-instantclient19.3-basic-19.3.0.0.0-1.x86_64.rpm

# python3 -> python
# pip3 -> pip
RUN    cd /usr/bin \
    && ln -sf python3 python \
    && ln -sf pip3 pip

COPY requirements.txt /usr/src/
WORKDIR /usr/src

#pip install
RUN    pip install --user --upgrade pip==18.1 \
    && pip install -r /usr/src/requirements.txt


