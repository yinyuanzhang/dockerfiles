FROM node:10.16.0
MAINTAINER tools@digital.trade.gov.uk

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

USER node

EXPOSE 8080

CMD [ "npm", "start" ]
