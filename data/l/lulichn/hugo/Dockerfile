FROM node:slim

ENV HUGO_VERSION 0.52

# Install HUGO
WORKDIR /tmp

RUN set -x \
	&& wget -O - https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz |  tar xvfz - \
	&& mv hugo /usr/bin/hugo


RUN mkdir /data
WORKDIR   /data

ENTRYPOINT ["/usr/bin/hugo"]

