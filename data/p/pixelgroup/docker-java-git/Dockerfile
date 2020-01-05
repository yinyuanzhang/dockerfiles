FROM openjdk:11.0.5-jdk
MAINTAINER Pixel GmbH <info@pixel.de>

ENV LANG C.UTF-8

RUN set -eux; \
    apt-get update \
    && apt-get upgrade --yes --no-install-recommends \
    ; \
    rm -rf /var/lib/apt/lists/*

RUN set -eux; \
    echo "Adding user and group" \
    && groupadd --system --gid 1000 java \
    && useradd --system --gid java --uid 1000 --shell /bin/bash --create-home java \
    && chown --recursive java:java /home/java

RUN java -version

USER java
WORKDIR /home/java
