FROM node:8-alpine
MAINTAINER Dario Caruso <dev@dariocaruso.info>
WORKDIR /app
COPY ./package.json /app
RUN npm i --production
COPY ./index.js /app
COPY ./server.js /app
COPY ./bower_components /app/bower_components
COPY ./views /app/views
CMD cd /app && npm run serve