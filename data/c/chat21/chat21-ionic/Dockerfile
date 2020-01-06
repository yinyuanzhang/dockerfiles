### STAGE 1: Build ###

# We label our stage as ‘builder’
FROM node:10-alpine as builder

RUN npm install -g ionic cordova@8.0.0

WORKDIR /app

COPY . ./

RUN npm install

RUN mkdir ./www

RUN cordova platform add browser@latest

RUN ionic cordova build browser

### STAGE 2: Setup ###

FROM nginx:1.14.1-alpine

## Copy our default nginx config
#COPY nginx/default.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/nginx.conf

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /app/platforms/browser/www/ /usr/share/nginx/html


WORKDIR /usr/share/nginx/html

RUN echo "Chat21 Ionic Started!!"


CMD ["nginx", "-g", "daemon off;"]



