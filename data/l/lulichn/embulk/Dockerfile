
FROM openjdk:8-jre-alpine

MAINTAINER lulichn <daisuke.develop@gmail.com>

ENV EMBULK_VERSION 0.8.31

RUN \
	apk --no-cache add --virtual deps curl && \
	curl -L https://dl.bintray.com/embulk/maven/embulk-$EMBULK_VERSION.jar --create-dirs -o /root/.embulk/bin/embulk && \
	chmod +x /root/.embulk/bin/embulk && \
	ln -s /root/.embulk/bin/embulk /usr/local/bin/embulk && \
	apk del deps && \
	apk --no-cache add jruby

