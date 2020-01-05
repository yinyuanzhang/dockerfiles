FROM node:8.10

MAINTAINER Asaf Kotzer <asaf@soluto.com>

RUN apt-get update \
    && apt-get install -y libsecret-1-dev \
    && git config --global user.email "it@soluto.com" \
    && git config --global user.name "it"
