FROM node:8-alpine

ENV NODE_ENV=production

RUN mkdir /app
WORKDIR /app

COPY package.json .

RUN yarn --production

COPY . .

CMD ["yarn", "start"]
