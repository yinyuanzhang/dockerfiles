FROM node:alpine
MAINTAINER rainu <rainu@raysha.de>

RUN apk --update --no-cache add git  &&\
    mkdir app && cd app &&\
    git clone https://github.com/mrvautin/adminMongo.git &&\
    cd adminMongo &&\
    npm install --production &&\
    apk del git

WORKDIR /app/adminMongo

CMD node app.js
EXPOSE 1234
