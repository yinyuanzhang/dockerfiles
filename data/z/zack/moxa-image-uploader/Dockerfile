FROM node:10-slim

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm ci --production

COPY . .

EXPOSE 8080

CMD [ "npm", "start" ]
