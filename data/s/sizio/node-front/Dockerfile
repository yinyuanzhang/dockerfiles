FROM node

MAINTAINER The Siz Team

RUN apt-get update && \
    apt-get install -y optipng ruby ruby-dev && \

    gem update --system && \
    gem install compass && \
    gem install oily_png && \

    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN npm install -g logentries-piper
