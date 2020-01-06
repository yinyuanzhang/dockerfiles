FROM node:carbon-alpine

COPY ./ /app
WORKDIR /app

RUN yarn

EXPOSE 3000

CMD [ "yarn", "start" ]