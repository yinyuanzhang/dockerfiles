FROM node:8.11.4-alpine
LABEL maintainer="Don Peter C. Atunalu <patunalu@yahoo.com>"
ARG NODE_ENV="production"
ARG PORT="80"
ARG NAME="ibanking"
ENV NODE_ENV ${NODE_ENV} \
    PORT ${PORT}
ADD . /app

WORKDIR /app
RUN npm i -g npm@latest &&\
    npm install && \
    npm i -g pm2
EXPOSE 80
CMD pm2-runtime start bin/www
