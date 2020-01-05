
###
# 1. Builder
###

FROM node:11-alpine as builder

ARG MAX_OLD_SPACE_SIZE=4096
ARG NPM_TOKEN
ENV NODE_OPTIONS=--max-old-space-size=${MAX_OLD_SPACE_SIZE}

WORKDIR /home/node

COPY package.json *package-lock.json *.npmrc ./

## Storing node modules on a separate layer will prevent unnecessary npm installs at each build
RUN npm ci

COPY . .

## Build the angular app in production mode and store the artifacts in dist folder
RUN npm run build-prod

###
# 2. Runner
###

FROM nginx:1.14-alpine

## Copy our default nginx config
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

## From 'builder' stage copy over the artifacts in dist folder to default nginx public folder
COPY --from=builder /home/node/dist/banzai-pipeline/ /usr/share/nginx/html/ui/
COPY docker-entrypoint.sh /docker-entrypoint.sh

ARG GIT_COMMIT=N/A
ENV API_URL=http://localhost
ENV GIT_COMMIT=${GIT_COMMIT}
ENV TAG=local
ENV FORMSPREE_FORM_ID=N/A
ENV CICD_SCM=github

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
