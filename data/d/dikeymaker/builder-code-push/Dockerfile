from debian:stretch-slim

RUN apt-get update && \
    apt-get install -y \
    	apt-utils \
        bash \
        git \
      	wget \
      	unzip \
      	xz-utils \
        expect \
    	expect-dev

RUN wget https://nodejs.org/dist/v10.16.0/node-v10.16.0-linux-x64.tar.xz \
    && mkdir /usr/local/lib/nodejs \
    && xz -d node-v10.16.0-linux-x64.tar.xz \
    && tar -xvf node-v10.16.0-linux-x64.tar \
    && mv node-v10.16.0-linux-x64 /usr/local/lib/nodejs \
    && export VERSION=v10.16.0 \
    && export DISTRO=linux-x64 \
    && export PATH=/usr/local/lib/nodejs/node-v10.16.0-linux-x64/bin:$PATH \
    && npm install -g code-push-cli

