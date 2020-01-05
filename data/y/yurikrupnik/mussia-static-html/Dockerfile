FROM node:alpine

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app
COPY root ./root
COPY package.json package-lock.json ./
RUN npm install
ENV ROOT_PATH root/
COPY server.js ./

CMD npm start
EXPOSE 80