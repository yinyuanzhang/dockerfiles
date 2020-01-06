FROM python:3-alpine3.9

LABEL maintainer="Thomas Grimonet"
LABEL com.example.version="1.0"
LABEL vendor1="Inetsix"
LABEL com.example.release-date="2019-05-07"
LABEL com.example.version.is-production="True"


ENV TERRAFORM_VERSION=0.11.13
ENV PACKER_VERSION=1.4.0

# update and install tools including python3
RUN set -x \
  echo "http://dl-6.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
  && apk update \
  && apk upgrade \
  && apk add curl wget unzip openrc git openntpd tzdata jq bash \
  && python --version; python3 --version; docker --version; git --version; jq --version

# set timezone to America/New_York
RUN set -x \
  && ls /usr/share/zoneinfo \
  && cp /usr/share/zoneinfo/Europe/Paris /etc/localtime \
  && echo "Europe/Paris" >  /etc/timezone \
  && date \
  && apk del tzdata

# install AWS cli
RUN set -x \
  && pip install awscli --upgrade \
  && exec bash

# confirm by checking vesion
RUN set -x \
  && aws --version

# install packer
RUN set -x \
  && curl -O "https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip" \
  && unzip packer_${PACKER_VERSION}_linux_amd64.zip \
  && rm -rf packer_${PACKER_VERSION}_linux_amd64.zip \
  && mv packer /usr/bin \
  && packer version

# Install terraform
RUN set -x \
  && curl -O "https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip" \
  && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
  && rm -rf terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
  && mv terraform /usr/bin \
  && terraform version


VOLUME ["/project"]
WORKDIR /project