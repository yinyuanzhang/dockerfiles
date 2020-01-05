FROM node:9.11-alpine

ENV YARN_VERSION 1.5.1

RUN mkdir /app

COPY orbit /app/orbit

COPY src /app/src

COPY .angular-cli.json \
  *.js \
  *.json \
  *.ts \
  yarn.lock \
  /app/

RUN cd /app \
  && yarn global add @angular/cli@1.7.3 \
  && yarn install --prod \
  && yarn cache clean \
  && yarn run build:ssr

EXPOSE 4000

WORKDIR /app
