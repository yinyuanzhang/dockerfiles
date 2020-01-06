FROM node:12.13-alpine

# Based on https://hub.docker.com/r/atlassian/pipelines-awscli

LABEL maintainer="Jerry Chang <jchang@assetic.com>"

RUN apk --update --no-cache add \
    build-base \
    ruby \
    ruby-dev \
    ruby-bundler \
    ruby-bigdecimal \
    python3 \
	python3-dev \
	libffi-dev \
	openssl-dev \
    jq \
    bash \
    git \
    groff \
    less \
    mailcap \
    bash \
    autoconf \
    libtool \
    nasm \
    automake \
    zlib-dev \
    zip \
    && pip3 install --no-cache-dir awscli boto3 \
    && rm -rf /var/cache/apk/* /root/.cache/pip/*

# Install bump cli
RUN gem install bump-cli --no-document\
    && gem install json --no-document \
    && gem cleanup \
    && rm -rf /usr/lib/ruby/gems/*/cache/*

WORKDIR /root
VOLUME /root/.aws

ENTRYPOINT [ "aws" ]
CMD ["--version"]