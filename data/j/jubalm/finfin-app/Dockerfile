FROM node:alpine

WORKDIR /usr/src/app

ENV API_ENDPOINT http://localhost:4000

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000
CMD [ "npm", "start" ]