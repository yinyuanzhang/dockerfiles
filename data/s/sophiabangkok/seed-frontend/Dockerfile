FROM sophiabangkok/seed-frontend as build
ARG NPM_TOKEN
ARG SERVICE_NAME

WORKDIR /app

## Cache package.json here so that
## we'll rebuild packages only when it changes
COPY package.json yarn.lock ./
RUN yarn install

## WE'll serve live assets from here
## NOTE: This is due to the way we serve items
##       from inside traefic. We use a prefix to
##       separate services and then slice the url.
ENV ASSET_PREFIX=/$SERVICE_NAME

## Copy all build specifics
COPY src pages .babelrc next* ./

## Now build our frontend sources
RUN yarn build

## Second build
## NOTE: Create a second layer where we copy only required
##       items across. Prevents accidental leak of git history
FROM node:current-alpine
WORKDIR /app

COPY --from=build /app/.next ./.next
COPY --from=build /app/package.json ./
COPY --from=build /app/node_modules ./node_modules

## Finally start the server
CMD yarn start
