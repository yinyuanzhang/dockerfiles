FROM openjdk:8-jre-alpine

MAINTAINER louay@alakkad.me

RUN apk update && apk add ca-certificates wget sudo && update-ca-certificates

RUN cd /tmp && \
    wget -nv https://downloads.crowdin.com/cli/v2/crowdin-cli.zip && \
    unzip crowdin-cli.zip && \
    mv 2.*/* ./ && \
    rm -rf 2.* crowdin-cli.zip *.bat && \
    chmod +x ./crowdin.sh && \
    ./crowdin.sh && \
    rm -rf *

COPY crowdin /usr/local/bin/crowdin

WORKDIR /tmp
