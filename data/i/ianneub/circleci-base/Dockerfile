FROM alpine:3.10
MAINTAINER Ian Neubert <ian@ianneubert.com>

RUN mkdir ~/repo
RUN apk --update add \ 
      less \
      groff \
      gcc \
      musl-dev \
      libffi-dev \
      openssl-dev \
      perl \
      python2 \
      python2-dev \
      py-pip \
      ruby \
      jq \
      curl \
      bash \
      make \
      docker \
      git \
      openssh-client && \
      pip install --upgrade requests awscli s3cmd docker-compose && \
      mkdir /root/.aws

WORKDIR ~/repo
