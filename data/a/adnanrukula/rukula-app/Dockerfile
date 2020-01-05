FROM ubuntu:14.04.2
MAINTAINER Adnan Issadeen <adnan.issadeen@live.com>

RUN apt-get update && apt-get install wget curl sqlite3 -y --force-yes 
RUN apt-get update && apt-get -y --force-yes build-dep python3.4
RUN mkdir /usr/src/python 
WORKDIR /usr/src/python
RUN wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz \
    && tar -xvf Python-3.4.3.tgz
WORKDIR /usr/src/python/Python-3.4.3
RUN ./configure \
    && make -j$(nproc) \
    && make altinstall
RUN pip3.4 install bcrypt Flask MonthDelta
WORKDIR /
