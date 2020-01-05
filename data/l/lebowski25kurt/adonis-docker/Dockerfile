FROM ubuntu:bionic

RUN apt-get update && apt-get install -yq --fix-missing zip unzip bash
RUN apt-get install -yq --fix-missing coreutils software-properties-common curl

RUN curl -sL https://deb.nodesource.com/setup_10.x |  bash
RUN apt-get install nodejs -y

RUN npm i -g @adonisjs/cli pm2 gulp yarn
