FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl software-properties-common && \
    (curl -sL https://deb.nodesource.com/setup_10.x | bash -) && \
    (curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -) && \
    (echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list) && \
    apt-get update -y && \
    apt-get install -y git curl build-essential zip unzip nodejs yarn && \
    hash -r -d npm && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.npm/cache/*

WORKDIR /code
