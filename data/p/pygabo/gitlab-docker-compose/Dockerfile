ARG DOCKER_VERSION=latest
FROM docker:${DOCKER_VERSION}

ARG COMPOSE_VERSION=
ARG DOCKER_VERSION

RUN apk add --no-cache py-pip python-dev libffi-dev openssl-dev gcc libc-dev make
RUN pip install "docker-compose${COMPOSE_VERSION:+==}${COMPOSE_VERSION}"
