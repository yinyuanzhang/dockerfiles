FROM node:12.13-alpine

# Versions: https://pypi.python.org/pypi/awscli#downloads
ENV AWS_CLI_VERSION 1.16.190
ENV TERRAFORM_VERSION=0.12.3
ENV TF_DEV=true
ENV TF_RELEASE=true

RUN apk --no-cache update && \
    apk --no-cache add \
	bash \
        python py-pip py-setuptools \
	git g++ make\
        ca-certificates groff less \
        musl-dev \
	sqlite-dev wget\
        bash openssh curl && \
    pip --no-cache-dir install awscli==${AWS_CLI_VERSION} && \
    rm -rf /var/cache/apk/*

RUN node --version
run npm --version

RUN npm cache clean --force && \
    npm -g install pm2 --no-optional

RUN curl -sL https://sentry.io/get-cli/ | bash

WORKDIR /tmp
RUN wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_386.zip && \
    unzip terraform_${TERRAFORM_VERSION}_linux_386.zip && \
    mv terraform /usr/bin/terraform &&\
    rm terraform_${TERRAFORM_VERSION}_linux_386.zip

WORKDIR /data
