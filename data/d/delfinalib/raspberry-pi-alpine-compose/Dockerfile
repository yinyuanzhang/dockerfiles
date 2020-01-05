ARG DOCKER_VERSION=18.09.7
ARG PYTHON_VERSION=3.7.4
ARG BUILD_ALPINE_VERSION=3.10
ARG BUILD_DEBIAN_VERSION=slim-stretch
ARG RUNTIME_ALPINE_VERSION=3.10.0
ARG RUNTIME_DEBIAN_VERSION=stretch-20190708-slim

ARG BUILD_PLATFORM=alpine

FROM delfinalib/raspberry-pi-alpine-docker AS docker-cli

FROM balenalib/raspberry-pi-alpine-python:3.7-3.7-build AS build-alpine

RUN [ "cross-build-start" ]
RUN apk add --no-cache \
    bash \
    build-base \
    ca-certificates \
    curl \
    gcc \
    git \
    libc-dev \
    libffi-dev \
    libgcc \
    make \
    musl-dev \
    openssl \
    openssl-dev \
    python2 \
    python2-dev \
    zlib-dev
RUN [ "cross-build-end" ]
ENV BUILD_BOOTLOADER=1

FROM build-${BUILD_PLATFORM} AS build
COPY docker-compose-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["sh", "/usr/local/bin/docker-compose-entrypoint.sh"]
COPY --from=docker-cli /usr/local/bin/docker /usr/local/bin/docker
WORKDIR /code/
# FIXME(chris-crone): virtualenv 16.3.0 breaks build, force 16.2.0 until fixed
RUN [ "cross-build-start" ]
RUN pip install virtualenv==16.2.0
RUN pip install tox==2.9.1

COPY requirements.txt .
COPY requirements-dev.txt .
COPY .pre-commit-config.yaml .
COPY tox.ini .
COPY setup.py .
COPY README.md .
COPY compose compose/
RUN tox --notest
COPY . .
ARG GIT_COMMIT=unknown
ENV DOCKER_COMPOSE_GITSHA=$GIT_COMMIT
RUN script/build/linux-entrypoint

RUN [ "cross-build-end" ]

FROM balenalib/raspberry-pi-alpine-python:3.7-3.7-run AS runtime-alpine
FROM runtime-${BUILD_PLATFORM} AS runtime
COPY docker-compose-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["sh", "/usr/local/bin/docker-compose-entrypoint.sh"]
COPY --from=docker-cli  /usr/local/bin/docker           /usr/local/bin/docker
COPY --from=build       /usr/local/bin/docker-compose   /usr/local/bin/docker-compose
