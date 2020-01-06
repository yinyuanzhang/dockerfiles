FROM node:8-alpine
WORKDIR /certifier
COPY ./ /certifier
RUN apk upgrade
RUN apk add --update --no-cache make gcc g++ python && npm install --prefix /certifier/backend && apk del make gcc g++ python
