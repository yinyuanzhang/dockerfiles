FROM node:10-alpine

MAINTAINER Bryce Anglin, <b.anglin@rapidnetworks.org>

ENV DAEMON_VERSION=v0.6.8

WORKDIR /srv/daemon

RUN apk add --no-cache curl openssl make gcc g++ python linux-headers paxctl gnupg tar zip unzip coreutils zlib \
 && curl -sSL https://github.com/Pterodactyl/Daemon/releases/download/${DAEMON_VERSION}/daemon.tar.gz -o daemon.tar.gz \
 && tar --strip-components=1 -xzvf daemon.tar.gz \
 && rm daemon.tar.gz \
 && npm install --production \
 && addgroup -S pterodactyl && adduser -S -D -H -G pterodactyl -s /bin/false pterodactyl \
 && apk del --no-cache make gcc g++ python linux-headers paxctl gnupg

EXPOSE 8080

CMD ["npm", "start"]
