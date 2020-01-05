FROM node:6.10

RUN mkdir -p /usr/src/app
COPY . /usr/src/app

WORKDIR /usr/src/app
RUN npm install -g bower
RUN npm install

WORKDIR /usr/src/app/client
RUN bower install

WORKDIR /usr/src/app
RUN mkdir logs

VOLUME /usr/src/app/client/uploads

CMD [ "npm", "start" ]