FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install virtualenv

RUN mkdir /root/nyar

ADD . /root/nyar 
RUN pip install -r /root/nyar/requirements.txt

RUN /root/nyar/test.py
