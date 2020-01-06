FROM tiangolo/node-frontend:10 as build-stage

ARG DOCKER_TAG
RUN export DOCKER_TAG=$DOCKER_TAG

WORKDIR /app
COPY package*.json /app/
RUN npm install
COPY ./ /app/
RUN npm run chromatic --exit-zero-on-changes
RUN npm run build


RUN npm install @sentry/cli
ENV SENTRY_AUTH_TOKEN=a5b8db140a83419b8c5f739ef2488ac858970d14c0fb49d592327156f71e5d27
ENV SENTRY_ORG=nexatlas-s2
ENV SENTRY_PROJECT=webapp
RUN ./node_modules/.bin/sentry-cli releases new $(./node_modules/.bin/sentry-cli releases propose-version) --project webapp
RUN ./node_modules/.bin/sentry-cli releases set-commits $(./node_modules/.bin/sentry-cli releases propose-version) --auto
RUN ./node_modules/.bin/sentry-cli releases files $(./node_modules/.bin/sentry-cli releases propose-version) upload-sourcemaps --no-rewrite build/static/js
RUN ./node_modules/.bin/sentry-cli releases finalize $(./node_modules/.bin/sentry-cli releases propose-version)
RUN ./node_modules/.bin/sentry-cli releases deploys $(./node_modules/.bin/sentry-cli releases propose-version) new -e $DOCKER_TAG


# Deploy stage
FROM nginx:alpine

COPY --from=build-stage /app/build/ /usr/share/nginx/html
COPY deployment/docker/nginx.conf /etc/nginx/nginx.conf