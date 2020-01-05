FROM node:alpine
MAINTAINER Joji Augustine "jojimail@gmail.com"

WORKDIR /app

COPY package.json /app
RUN npm install
EXPOSE 6001

CMD ["/app/node_modules/.bin/laravel-echo-server", "start"]