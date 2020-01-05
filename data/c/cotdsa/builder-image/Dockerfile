FROM python:3-alpine3.7

ENV DOCKER_CHANNEL stable
ENV DOCKER_VERSION 18.03.1-ce

# Python changed their image, this is for backwards compat
RUN ln -s /usr/local/bin/python /usr/bin/python

RUN set -ex; \
    apk add --no-cache --virtual .fetch-deps \
        curl \
        tar \
    ; \
    curl -fL -o docker.tgz "https://download.docker.com/linux/static/${DOCKER_CHANNEL}/x86_64/docker-${DOCKER_VERSION}.tgz"; \
    tar --extract \
        --file docker.tgz \
        --strip-components 1 \
        --directory /usr/local/bin/ \
    ; \
    rm docker.tgz; \
    apk del .fetch-deps; \
    dockerd -v; \
    docker -v

RUN set -xe && \
    apk add --no-cache tar git openssh-client jq curl && \
    pip install awscli boto yamllint && \
    true

RUN set -xe && \
    apk add --no-cache ansible && \
    true
