FROM node:11-alpine

COPY package.json /opt/amtsblatt-mailer/
WORKDIR /opt/amtsblatt-mailer
RUN npm install

COPY . /opt/amtsblatt-mailer/

CMD node amtsblatt-mailer.js
