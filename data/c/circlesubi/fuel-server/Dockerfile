FROM node

WORKDIR /usr/src/app

MAINTAINER Ed Zillion <edzillion@gmail.com>

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 6000
CMD [ "npm", "start" ]
