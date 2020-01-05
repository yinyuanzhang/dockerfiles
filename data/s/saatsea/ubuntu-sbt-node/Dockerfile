FROM ubuntu:19.04

ENV JDK_VERSION 11

# Prepare java+sbt
RUN apt-get update && apt-get install -y gnupg ca-certificates apt-transport-https fakeroot && \
	echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list && \
	apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823 && \
	apt-get update && apt-get install -y openjdk-$JDK_VERSION-jdk-headless sbt && \
	apt-get install -y curl && \
	rm -rf /var/lib/apt/lists/*

# Prepare node+npm
#RUN apt-get update && apt-get install -y curl apt-utils bzip2 && \
#	curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
#	apt-get update && apt-get install -y nodejs && \
#	rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y nodejs && \
	rm -rf /var/lib/apt/lists/*

# Chromium for integration tests
RUN apt-get update && apt-get install -y chromium-browser chromium-chromedriver && \
	rm -rf /var/lib/apt/lists/*

RUN curl -sL https://sentry.io/get-cli/ | bash

RUN touch /DOCKER_CI
