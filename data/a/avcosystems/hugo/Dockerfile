FROM node:8.11.2-stretch

RUN apt-get update
RUN apt-get install -y git ca-certificates

ADD https://github.com/gohugoio/hugo/releases/download/v0.46/hugo_0.46_Linux-64bit.tar.gz /tmp
RUN tar -xf /tmp/hugo_0.46_Linux-64bit.tar.gz -C /tmp \
    && mv /tmp/hugo /usr/local/bin/hugo \
&& rm -rf /tmp/*
