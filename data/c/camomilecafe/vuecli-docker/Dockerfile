FROM node:latest

RUN apt-get update
RUN npm install yarn
RUN apt-get install -y vim
RUN yarn global add @vue/cli

WORKDIR /var/www/html
