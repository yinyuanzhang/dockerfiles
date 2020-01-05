
FROM node:10-alpine as build-env

RUN apk add --no-cache git

RUN mkdir -p /srv/minecraft
WORKDIR /srv/minecraft
COPY package*.json ./
RUN npm install

FROM timbru31/java-node
RUN mkdir -p /srv/minecraft
WORKDIR /srv/minecraft
COPY --from=build-env /srv/minecraft .
COPY . .

CMD ["npm","start"]
