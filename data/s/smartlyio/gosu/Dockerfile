FROM debian:jessie-slim AS gosu

ENV GOSU_VERSION=1.10

RUN set -ex; \
      apt-get update; \
      apt-get --assume-yes --no-install-recommends install \
        ca-certificates \
        curl \
      ; \
      curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)"; \
      curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc"; \
      export GNUGPGHOME="$(mktemp -d)"; \
      gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4; \
      gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \
      chmod +x /usr/local/bin/gosu; \
      gosu nobody true; \
      rm --recursive --force /var/lib/apt/lists/* "$GNUGPGHOME" /usr/local/bin/gosu.asc;

COPY ./1.10/debian/docker-entrypoint.sh /gosu-entrypoint.sh
