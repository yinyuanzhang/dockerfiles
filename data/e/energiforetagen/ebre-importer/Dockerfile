FROM node:12.4-alpine as builder
RUN apk add --update python build-base && rm -rf /var/cache/apk/*

WORKDIR /app

COPY package* ./
RUN npm install
RUN apk del python build-base

COPY . .
RUN node_modules/typescript/bin/tsc

RUN ls -A | grep -v dist | xargs rm -rf
RUN find dist -type d -name '__*' -exec rm -r {} +;

#
#
#
FROM node:12.4-alpine as app
RUN apk add --update python build-base && rm -rf /var/cache/apk/*

WORKDIR /app

COPY --from=builder /app/dist ./dist

COPY templates ./dist/templates
COPY migrations ./dist/migrations

COPY package* ./
RUN npm install --production
RUN apk del python build-base

CMD node dist/src/index.js
