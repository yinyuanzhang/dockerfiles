# see: https://github.com/mhart/alpine-node
FROM mhart/alpine-node:12 as node
#FROM registry.cn-beijing.aliyuncs.com/recurrent/yarn:12

# see https://github.com/docker/compose/releases for the latest release version id
ENV COMPOSE_VERSION 1.23.2

RUN apk add --no-cache python3 bash ca-certificates git miniperl  \
        openssh-client rsync curl docker && \
    pip3 install --no-cache-dir docker-compose==${COMPOSE_VERSION}

