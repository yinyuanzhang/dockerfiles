FROM circleci/node:10.13.0

LABEL maintainer="dixahq"

RUN set -x \
    && sudo apt-get -y -qq update \
    && sudo apt-get install -y python3-pip python3-dev build-essential \
    && sudo pip3 install --upgrade awscli==1.16.230 \
    && sudo rm -rf /var/lib/apt/lists/*
