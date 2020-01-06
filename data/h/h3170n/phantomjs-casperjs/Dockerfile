FROM node:latest
MAINTAINER Helton Carlos de Souza <helton.development@gmail.com>
RUN apt-get update && \
	apt-get install -y python3 && \
	npm install -g phantomjs casperjs && \
	rm -rf /var/lib/apt/lists/*
