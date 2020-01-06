# Step 1: crea la imagen
FROM node:12.12-alpine AS builder

WORKDIR /usr/src/app
COPY . .
RUN yarn && yarn build

# Step 2: Usa la imagen
FROM nginx:stable-alpine
LABEL version="1.0"
COPY nginx.conf /etc/nginx/nginx.conf
WORKDIR /usr/share/nginx/html
COPY dist/angular-docker/ .


