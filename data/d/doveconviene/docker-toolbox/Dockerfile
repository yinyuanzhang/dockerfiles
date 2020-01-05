FROM docker:18.03.0-ce-dind

ENV DOCKER_COMPOSE_VERSION=1.20.1

RUN apk add --no-cache \
    git openssh-client \
    py-pip python-dev libffi-dev openssl-dev gcc libc-dev make \
    && pip install docker-compose==$DOCKER_COMPOSE_VERSION
