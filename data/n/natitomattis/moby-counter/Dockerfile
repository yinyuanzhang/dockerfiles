FROM node:10.12.0-slim

LABEL maintainer="workshop2018" \
      description="Simple nodejs app that desplays docker whales" \
      original_image="russmckendrick/docker"

ADD . /srv/app
WORKDIR /srv/app
RUN npm install

EXPOSE 80

ENTRYPOINT ["node", "index.js"]
