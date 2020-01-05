FROM node:7.8.0-slim

MAINTAINER Mazedur Rahman <mazedur.rahman.liton@gmail.com>

ENV PHANTOMJS_VERSION=2.1.1

RUN apt-get update \
	&& apt-get install -y \
	bzip2 \
	libfontconfig \
	&& apt-get clean \
	&& rm -rf /tmp/* /var/lib/apt/lists/*

RUN mkdir /tmp/phantomjs \
	&& curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2 \
		| tar -xj --strip-components=1 -C /tmp/phantomjs \
	&& mv /tmp/phantomjs/bin/phantomjs /usr/bin \
	&& rm -rf /tmp/phantomjs

ENTRYPOINT ["phantomjs"]
