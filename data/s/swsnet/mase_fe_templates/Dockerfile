FROM keymetrics/pm2:latest-alpine

ENV SERVERPREFIX /mase_templates
ENV HTTP_PORT 3300

COPY . /data
WORKDIR /data

LABEL traefik.enable "true"
LABEL traefik.frontend.rule "Path: $SERVERPREFIX"
LABEL traefik.frontend.entryPoints "https"
LABEL traefik.protocol "http"
LABEL traefik.port "$HTTP_PORT"

RUN apk add --no-cache --update alpine-sdk python
RUN npm install --production

CMD [ "pm2-runtime" , "start" , "docker.config.js" ]