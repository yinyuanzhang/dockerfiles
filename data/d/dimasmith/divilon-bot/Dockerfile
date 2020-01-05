FROM node:carbon-alpine
MAINTAINER Dmytro Kovalchuk <dmytro.kovalchuk@divilon.com.ua>

EXPOSE 3000

RUN mkdir /app
WORKDIR /app

COPY yarn.lock package.json bot.js ./
RUN yarn

ENV NODE_ENV=production

CMD [ "node", "bot.js" ]