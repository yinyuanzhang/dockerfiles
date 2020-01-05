FROM node:latest

MAINTAINER gajjargaurav@gmail.com

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN npm install

EXPOSE 1337

CMD ["npm", "start"]
