FROM ubuntu:bionic

RUN apt-get update \
    && apt-get install -y tzdata libcurl4 libssl-dev \
    && rm -r /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false