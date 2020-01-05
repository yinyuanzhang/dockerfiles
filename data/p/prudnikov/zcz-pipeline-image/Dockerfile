FROM ubuntu:xenial
MAINTAINER Vladimir Prudnikov, v.prudnikov@gmail.com

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update 
RUN apt-get upgrade -y
RUN apt-get install -y apt-utils gcc openssh-client rsync git
RUN apt-get install -y python3.5 
RUN apt-get install -y python3.5-dev

RUN ln -s /usr/bin/python3.5 /usr/bin/python


# AWS CLI needs the PYTHONIOENCODING environment varialbe to handle UTF-8 correctly:
ENV PYTHONIOENCODING=UTF-8

RUN apt-get install -y man curl sudo 
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
RUN apt-get install -y nodejs
RUN apt-get install -y less
RUN apt-get install -y python-virtualenv
RUN apt-get install -y postgresql
RUN apt-get install -y postgresql-contrib 
RUN apt-get install -y libpq-dev
RUN apt-get install -y gettext

RUN npm install -g webpack bower gulp

RUN virtualenv /env

WORKDIR /app

# ADD requirements.txt .
# ADD package.json .
# #RUN /env/bin/pip install -r requirements.txt
# #RUN pip install awscli boto3 


# RUN npm install
