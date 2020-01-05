FROM node:10.14.2-alpine

WORKDIR /usr/src/app

COPY package*.json ./

RUN yarn config set scripts-prepend-node-path true

RUN yarn

COPY . .

RUN yarn build:ssr

EXPOSE 8080

CMD [ "yarn", "serve:ssr" ]

