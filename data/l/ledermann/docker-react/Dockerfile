# Build with Node.JS
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install
COPY . .
RUN yarn build
RUN CI="true" yarn test

# Production with Nginx
FROM nginx:stable-alpine
LABEL maintainer="mail@georg-ledermann.de"
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /app/build /usr/share/nginx/html
