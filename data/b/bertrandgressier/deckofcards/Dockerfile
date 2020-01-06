### STAGE 1: Build ###

# We label our stage as 'builder'
FROM docker.io/node:8-stretch as builder

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends chromium

ENV CHROME_BIN=chromium

RUN npm install -g @angular/cli

COPY package*.json ./

RUN npm set progress=false && npm config set depth 0 && npm cache clean --force

## Storing node modules on a separate layer will prevent unnecessary npm installs at each build
RUN npm i && mkdir /ng-app && cp -R ./node_modules ./ng-app

WORKDIR /ng-app

COPY . .

## verify lint
RUN ng lint

## Run unit test
RUN ng test --browsers ChromeHeadlessCI --code-coverage=true --watch=false

## Build the angular app in production mode and store the artifacts in dist folder
RUN ng build --prod --build-optimizer


### STAGE 2: Setup ###

FROM nginx:1.13.3-alpine

## Copy our default nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

## From 'builder' stage copy over the artifacts in dist folder to default nginx public folder
COPY --from=builder /ng-app/dist/deckOfCards /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
