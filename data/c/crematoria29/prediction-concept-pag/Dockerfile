FROM node:10-alpine

WORKDIR /usr/src/app

COPY package.json ./

RUN npm install

COPY . .

ENV API_URL http://137.182.193.50:8000

EXPOSE 8000

CMD [ "npm", "start" ]
