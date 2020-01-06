FROM sophiabangkok/seed-microservice as build
ARG NPM_TOKEN

## Add package.json here so that
## we'll rebuild packages only when it changes
COPY package.json yarn.lock ./

## Add our npm credentials
## Run the production installation
## Then remove our credentials again
## NOTE: This is necessary to prevent leaking our
##       NPM credentials through public packages
RUN echo "//registry.npmjs.org/:_authToken=$NPM_TOKEN" > .npmrc && \
    yarn install --production && \
    rm -f .npmrc;

## Now move everything over so that we can easily reference anything we want
COPY . ./

## Second build
## NOTE: Create a second layer where we copy only required
##       items across. Prevents accidental leak of git history
FROM node:current-alpine

WORKDIR /app

## Copy configuration
COPY --from=build moleculer.config.js ./

## Copy directories across
COPY --from=build services ./services
COPY --from=build node_modules ./node_modules

CMD yarn start
