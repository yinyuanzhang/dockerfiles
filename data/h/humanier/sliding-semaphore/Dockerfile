FROM node:alpine

EXPOSE 3000

RUN apk add bash

RUN mkdir -p /usr/bin/sliding-semaphore

COPY . /usr/bin/sliding-semaphore

WORKDIR /usr/bin/sliding-semaphore

RUN npm ci --only=prod

CMD [ "src/server.js" ]