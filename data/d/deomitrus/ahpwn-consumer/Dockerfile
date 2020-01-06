# DOCKER-VERSION 1.1.2

# IMPORTS
FROM ubuntu:latest
FROM node:latest

# DIRS
ADD . /app
WORKDIR /app

# INSTALL DEPENDENCIES
RUN cd /app
RUN npm install

# CMD
CMD [ "node", "consumer.js" ]
