FROM alpine:latest

MAINTAINER Cédric Stanislas <nori971@gmail.com>

LABEL Description="DevOps Tooling environnement" Version="0.2"

ENV TERRAFORM_VERSION=0.12.3
# Alpine-based installation
# #########################
RUN apk add --update \
  python-dev \
  curl \
  unzip \
  zip \
  py-pip \
  py-setuptools \
  ca-certificates \
  gcc \
  libffi-dev \
  openssl-dev \
  musl-dev \
  linux-headers \
  dmidecode \
  bash \
  && apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/testing git-crypt \
  && pip install --upgrade --no-cache-dir pip setuptools python-keystoneclient python-glanceclient python-novaclient python-openstackclient \
  && apk del gcc musl-dev linux-headers libffi-dev \
  && curl -sSL https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -o /tmp/terraform.zip \
  && unzip /tmp/terraform.zip -d /usr/bin \
  && rm -rf  /tmp/terraform.zip /var/cache/apk/*

