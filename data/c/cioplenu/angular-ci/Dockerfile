FROM node:10.16-stretch

LABEL maintainer="Anian Ziegler" \
      email="it@cioplenu.de"

RUN apt-get update                                                                                             \
    && apt-get install -y chromium git wget unzip jq                                                           \
    && yarn global add @angular/cli --network-timeout 100000                                                   \
    && git config --global user.email "git@localhost"                                                          \
    && git config --global user.name "git"

COPY assets/* /opt/

ENV CHROME_BIN=/usr/bin/chromium

