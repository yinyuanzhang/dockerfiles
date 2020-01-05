FROM node:alpine

ARG CLIENT_URL
ARG SERVER_URL
ARG TIME_URL

ENV PTC_CLIENT_URL $CLIENT_URL
ENV PTC_SERVER_URL $SERVER_URL
ENV PTC_TIME_URL $TIME_URL

ENV PTC_SERVER_PORT=3000
ENV PTC_TIME_DIR=/app/time
ENV PTC_MANAGE_DIR=/app/manage
ENV PTC_STATIC_DIR=/static

EXPOSE 3000
VOLUME ["/app", "/import", "/static"]

WORKDIR /home/node/pentacode

# Only copy over the packages files of all required packages.
# This will ensure that we don't have to install all dependencies
# again if any source files change.
COPY package*.json lerna.json tsconfig.json ./
COPY packages/core/package*.json ./packages/core/
COPY packages/server/package*.json ./packages/server/
COPY packages/app/package*.json ./packages/app/
COPY packages/time/package*.json ./packages/time/

# Install dependencies and bootstrap packages
RUN npm ci --unsafe-perm

# Now copy over source files and assets
COPY packages/core/src ./packages/core/src
COPY packages/core/tsconfig.json ./packages/core/

COPY packages/server/src ./packages/server/src
COPY packages/server/migrations ./packages/server/migrations
COPY packages/server/tsconfig.json ./packages/server/
COPY packages/server/ormconfig.json ./packages/server/

COPY packages/app/src ./packages/app/src
COPY packages/app/vendor ./packages/app/vendor
COPY packages/app/types ./packages/app/types
COPY packages/app/tsconfig.json ./packages/app/
COPY packages/app/webpack.config.js ./packages/app/

COPY packages/time/src ./packages/time/src
COPY packages/time/tsconfig.json ./packages/time/
COPY packages/time/webpack.config.js ./packages/time/

CMD npm run build & npm start
