FROM docker
ARG DAEMON_VERSION="v0.6.12"
ARG GID="500"
ARG UID="500"

WORKDIR /srv/daemon
RUN apk add --no-cache --virtual=build-dependencies curl g++ gcc make python python-dev && \
     apk add --no-cache nodejs npm tar unzip zip && \
     mkdir -p /srv/daemon /srv/daemon-data && \
     addgroup -S -g ${GID} pterodactyl && \
     adduser -S -D -H -g "Pterodactyl Daemon" -G pterodactyl -u ${UID} -s /bin/false pterodactyl && \
     curl -Lo /tmp/daemon.tar.gz https://github.com/Pterodactyl/Daemon/archive/${DAEMON_VERSION}.tar.gz && \
     tar --strip-components=1 -xzvf /tmp/daemon.tar.gz -C /srv/daemon/ && \
     npm install --production && \
     apk del --purge build-dependencies && \
     rm -rf /root/.npm /root/.node-gyp /var/cache/apk/* /tmp/*

EXPOSE 2022 8443
VOLUME /srv/daemon/config /srv/daemon/packs /srv/daemon-data

CMD ["npm", "start"]