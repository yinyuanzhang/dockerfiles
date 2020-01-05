#FROM python:3.6-alpine # having trouble installing numpy on alpine linux... using ubuntu

FROM ubuntu:18.04
RUN apt-get -qq update
RUN apt-get -qq -y install python3
RUN apt-get -qq -y install python3-pip
RUN apt-get -qq -y install python3-gdal gdal-bin
RUN alias python=python3


# Fix error https://stackoverflow.com/questions/48179961/runtimeerror-npm2deb-will-abort-further-execution-because-python-3-was-configur
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /home/cltixapp

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn pymysql
