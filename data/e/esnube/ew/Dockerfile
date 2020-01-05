# pull official base image
FROM node:slim

# make dir
RUN mkdir /usr/src/app

# set work directory
WORKDIR /usr/src/app

# copy project
COPY . /usr/src/app/

# install dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
         g++ \
         build-essential \
         python3 \
         procps  \
         joe

# set environment variables
ENV LC_CTYPE es_ES.UTF-8
ENV LANG es_ES.UTF-8
ENV APP_ROOT /src
ENV HOST 0.0.0.0

# update packages
RUN rm yarn.lock
RUN yarn install
