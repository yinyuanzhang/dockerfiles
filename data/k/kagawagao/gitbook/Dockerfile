FROM node:10

ARG VERSION=3.2.3

ARG DEBIAN_FRONTEND=noninteractive

LABEL maintainer=kingsongao1221@gmail.com

LABEL version=$VERSION

RUN apt-get update

RUN apt-get install -y --no-install-recommends apt-utils

RUN apt-get install -y -qq sshpass

RUN apt-get install -y sudo

# install gitbook-cli
RUN npm install -g gitbook-cli

# install gitbook
RUN gitbook fetch ${VERSION}
