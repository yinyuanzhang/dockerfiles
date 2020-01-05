FROM python:3.6.1
MAINTAINER Vladimir Prudnikov, v.prudnikov@gmail.com

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y apt-utils openssh-client rsync git


# AWS CLI needs the PYTHONIOENCODING environment varialbe to handle UTF-8 correctly:
ENV PYTHONIOENCODING=UTF-8

RUN apt-get install -y man curl sudo
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
RUN apt-get install -y nodejs less python-virtualenv postgresql postgresql-contrib libpq-dev gettext wkhtmltopdf

RUN npm install -g webpack gulp gulp-scss

# RUN virtualenv /env

WORKDIR /app

ADD requirements.txt .
ADD package.json .
RUN pip install -r requirements.txt
RUN pip install awscli boto3
RUN pip install -I Django==1.11.4
RUN pip install -I djangorestframework==3.6.4

RUN npm install
