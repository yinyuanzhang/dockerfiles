FROM ubuntu:16.04

MAINTAINER Anush

# ---------------------------
# --- Install required tools

RUN apt-get update -y && \
	apt-get install -y \
		curl \
		git \
		expect \
		wget \
		zip \
		unzip

RUN apt-get clean

ENV NODEJS_VERSION=8.3.0 \
    PATH=$PATH:/opt/node/bin

# Installing Node
RUN curl -sL https://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}-linux-x64.tar.gz | tar xz --strip-components=1 
RUN rm -rf /var/lib/apt/lists/*

# Installing Yarn npm package manager
RUN npm i -g yarn 
