# STEP 1: Build
# FROM node:8-alpine as builder
FROM node:8.16.0-alpine as builder

LABEL authors="cipchk <cipchk@qq.com>"

COPY package.json ./

RUN npm set progress=false && npm config set depth 0 && npm cache clean --force
RUN npm i && mkdir /ng-alain && cp -R ./node_modules ./ng-alain

WORKDIR /ng-alain

COPY . .

RUN npm install
RUN npm run build:prod

# STEP 2: Setup
FROM nginx:1.13.5-alpine

COPY --from=builder /ng-alain/_nginx/default.conf /etc/nginx/conf.d/default.conf

RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /ng-alain/www /usr/share/nginx/html

COPY --from=builder /ng-alain/www/assets/MP_verify_stK6vtetnWy5wQDY.txt /usr/share/nginx/html
COPY --from=builder /ng-alain/www/assets/MP_verify_PVgZ963NcrVs8LE8.txt /usr/share/nginx/html

CMD [ "nginx", "-g", "daemon off;"]
