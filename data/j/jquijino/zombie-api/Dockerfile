### BUILD
FROM node:12-alpine AS build

### SET TIMEZONE
RUN apk add --no-cache tzdata
#RUN npm install npm@latest -g
RUN cp /usr/share/zoneinfo/UTC /etc/localtime
RUN echo "UTC" >  /etc/timezone

WORKDIR /app
COPY . .

### BUILD_DEV
FROM build AS builddev
RUN npm install

### BUILD_PROD
FROM builddev AS buildprod
RUN npm prune --production

### BASE
FROM node:8-alpine AS base
WORKDIR /app
#HEALTHCHECK --interval=20s --timeout=2s CMD curl --fail http://localhost:5000/health || exit 1
USER node

### DEV
FROM build AS dev
COPY --from=builddev --chown=node:node /app /app
CMD ["npm", "start"]

### PROD
FROM base AS prod
COPY --from=buildprod --chown=node:node /app /app
CMD ["node", "bot.js"]
