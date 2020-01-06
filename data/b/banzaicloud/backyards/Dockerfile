ARG NODE_VERSION=12
ARG NGINX_VERSION=1.15
ARG MAX_OLD_SPACE_SIZE=4096

###
# 1. Builder
###

FROM node:${NODE_VERSION}-alpine as builder
WORKDIR /home/node/

RUN apk update && \
  apk add --virtual build-dependencies \
  build-base \
  gcc \
  wget \
  git \
  python
RUN npm install --global npm node-gyp

COPY package.json *package-lock.json *.npmrc ./

RUN npm ci
ARG NODE_ENV=production
ENV NODE_ENV ${NODE_ENV}

COPY . .
RUN npm run build

###
# 2. Application
###

FROM nginx:${NGINX_VERSION}-alpine
WORKDIR /home/node/

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

COPY docker-entrypoint.sh /docker-entrypoint.sh

## From 'builder' stage copy over the artifacts in dist folder to default nginx public folder
COPY --from=builder /home/node/dist/backyards/ /usr/share/nginx/html/

ENV PATH="/home/node/node_modules/.bin:${PATH}"
ENV NODE_ENV production
ENV PORT 80
ENV API_URL=/api

EXPOSE ${PORT}

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
