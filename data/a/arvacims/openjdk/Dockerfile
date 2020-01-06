FROM openjdk:11.0.3-jre-slim-stretch

RUN apt-get update \
    && apt-get --yes --no-install-recommends install curl wget \
    && apt-get --yes autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/*
