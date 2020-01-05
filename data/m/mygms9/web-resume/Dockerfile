FROM node:8.12.0-jessie

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install
RUN npm install react-scripts -g

COPY . /usr/src/app

CMD [ "npm", "start" ]
