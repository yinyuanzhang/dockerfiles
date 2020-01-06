FROM node:carbon

MAINTAINER dreamsnail@gmail.com

RUN mkdir -p /buyweb

WORKDIR /buyweb

ADD ./ /buyweb

RUN npm install

ENV NODE_ENV=production

CMD node app.js
