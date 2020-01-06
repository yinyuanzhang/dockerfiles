FROM node:10

WORKDIR /home/node/app

VOLUME .:/home/node/app

COPY package*.json ./

RUN npm i

COPY . .

EXPOSE 9999

CMD [ "node", "index" ]