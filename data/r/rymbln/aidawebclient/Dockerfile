### STAGE 1: Build ###

# We label our stage as 'builder'
FROM node:10.16.3-alpine as builder

COPY package.json package-lock.json ./

RUN npm set progress=false && npm config set depth 0 && npm cache clean --force

## Storing node modules on a separate layer will prevent unnecessary npm installs at each build
RUN npm i && mkdir /ng-app && cp -R ./node_modules ./ng-app

WORKDIR /ng-app

COPY . .

## Build the angular app in production mode and store the artifacts in dist folder
#RUN $(npm bin)/npm run build:ssr
#RUN npm run build:ssr && npm run serve:ssr


### STAGE 2: Setup ###

# FROM nginx:1.13.3-alpine

## Copy our default nginx config
# COPY nginx/default.conf /etc/nginx/conf.d/

## Remove default nginx website
# RUN rm -rf /usr/share/nginx/html/*

## From 'builder' stage copy over the artifacts in dist folder to default nginx public folder
#COPY --from=builder /ng-app/dist /usr/share/nginx/html

#CMD ["nginx", "-g", "daemon off;"]

## --
## ## THIS IS STATIC RENDERER
## --

# RUN npm run build:static

# FROM node:8-alpine
# RUN npm install http-server -g
# COPY --from=builder /ng-app/dist /dist
# WORKDIR /dist/browser
# CMD ["http-server"]

## -- 
## ## THIS IS DINAMIC RENDERER ## ##
## --

RUN npm run build:dynamic
FROM node:10.16.3-alpine
COPY --from=builder /ng-app/dist /dist
CMD ["node", "/dist/server"]


### --- 
## Static NginX Server instead of static http-server
### ---
# RUN npm run build:dynamic
# FROM nginx:1.13.3-alpine
# COPY nginx/default.conf /etc/nginx/conf.d/
# RUN rm -rf /usr/share/nginx/html/*
# COPY --from=builder /ng-app/dist/browser /usr/share/nginx/html
# CMD ["nginx", "-g", "daemon off;"]