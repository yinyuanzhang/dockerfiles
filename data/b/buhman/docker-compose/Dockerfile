FROM docker:latest

ENV COMPOSE_VERSION 1.16.0-rc1

RUN set -ex; \
    apk add --no-cache --virtual .build-deps \
		python3 git \
    ; \
    pip3 install docker-compose==$COMPOSE_VERSION; \
    docker-compose -v
