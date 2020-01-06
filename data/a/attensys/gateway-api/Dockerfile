FROM node:6.12.3-alpine

ENV NODE_ENV production

RUN apk update && apk add git python make g++ curl

WORKDIR /usr/src/app

COPY ["package.json", "npm-shrinkwrap.json*", "./"]
RUN npm install --production --silent && mv node_modules ../

COPY . .

EXPOSE 7080

CMD [ "npm", "start" ]