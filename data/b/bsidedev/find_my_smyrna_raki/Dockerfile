FROM node:8.11.2
MAINTAINER Okechi Onyeje <o.onyeje@gmail.com>

ARG '-p 3010:3010 -p 5010:5010'

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -y install autoconf automake libtool nasm make pkg-config git apt-utils

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Versions
RUN npm -v
RUN node -v

# Install app dependencies
COPY package.json /usr/src/app/
COPY package-lock.json /usr/src/app/

RUN npm install

# Bundle app source
COPY . /usr/src/app

EXPOSE 3010
EXPOSE 5010

# Environment variables
ENV NODE_ENV production
ENV PUBLIC_PATH "/"

CMD [ "npm", "run", "prod" ]

