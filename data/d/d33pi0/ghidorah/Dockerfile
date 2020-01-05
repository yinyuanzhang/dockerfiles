FROM node:12.6.0-alpine

# COPY package.json package-lock.json /code/ghidorah/
COPY package.json /code/ghidorah/
COPY ./public /code/ghidorah/public
COPY ./src /code/ghidorah/src 

RUN cd /code/ghidorah \
  && yarn install

ENV HOST=0.0.0.0
