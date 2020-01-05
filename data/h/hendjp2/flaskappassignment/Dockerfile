FROM ubuntu:16.04
MAINTAINER Josh <Hendjp1@student.op.ac.nz>
ENV updated_on "2018-08-14 900"
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install python3 python3-setuptools python3-pip gunicorn3
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10
COPY . /flaskapp
WORKDIR /flaskapp
RUN pip3 install -r requirements.txt
EXPOSE 5000
