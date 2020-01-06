FROM node:lts-alpine
RUN apk add --no-cache bind
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install --only-production

COPY . .

CMD [ "npm", "start" ]
