FROM node:8

RUN mkdir /app
WORKDIR /app
COPY package.json /app
RUN npm install -g nodemon
RUN npm install

COPY . /app

ENV SERVICE={$SERVICE}
CMD ["nodemon", "server.js"]
