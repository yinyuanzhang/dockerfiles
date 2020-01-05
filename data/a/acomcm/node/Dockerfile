FROM ubuntu:xenial
MAINTAINER Ivan <ivan.petrus@acommerce.asia>

COPY sources.list /etc/apt
RUN apt-get update && apt-get install -y curl libfontconfig python build-essential git && apt-get autoclean

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN echo Node 6.10.2 && \
    curl -sL https://deb.nodesource.com/setup_6.x | bash -

RUN apt-get install -y nodejs && apt-get autoclean

RUN npm install -g bower gulp phantomjs-prebuilt eslint node-gyp && \
    npm cache clean && \
    bower --allow-root cache clean

WORKDIR /app
