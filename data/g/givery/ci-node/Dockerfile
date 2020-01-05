FROM node:10-slim

WORKDIR /workspace

RUN apt-get update \
	&& apt-get install -y \
		build-essential \
		python3 \
		python3-pip \
		curl \
		git \
		zip \
	&& rm -rf /var/lib/apt/list/* \
	&& pip3 install awscli --upgrade \
	&& curl -sSfL https://install.goreleaser.com/github.com/tj/node-prune.sh | sh -s -- -b /usr/local/bin
