FROM node:12-alpine

RUN npm i -g standard-version@6.0.1 && \
    apk update && apk upgrade && \
    apk add --no-cache git openssh

WORKDIR /app

ENTRYPOINT ["standard-version"]
