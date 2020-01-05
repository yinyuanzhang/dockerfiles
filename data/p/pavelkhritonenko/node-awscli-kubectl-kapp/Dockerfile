FROM node:12-alpine

RUN apk --no-cache add alpine-sdk curl bash git make musl-dev docker python py-pip openssh

ARG KUBECTL_VERSION=v1.16.0

# Install kubectl

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \
    && mv kubectl /usr/local/bin \
    && chmod +x /usr/local/bin/kubectl

ARG AWS_CLI_VERSION=1.16.248

# Install awscli
RUN pip install "awscli>=${AWS_CLI_VERSION}" --force

RUN curl -O https://amazon-eks.s3-us-west-2.amazonaws.com/1.11.5/2018-12-06/bin/linux/amd64/aws-iam-authenticator \
    && mv aws-iam-authenticator /usr/local/bin \
    && chmod +x /usr/local/bin/aws-iam-authenticator

ARG KAPP_VERSION=v0.13.0 

RUN curl -OL https://github.com/k14s/kapp/releases/download/${KAPP_VERSION}/kapp-linux-amd64 \
    && mv kapp-linux-amd64 /usr/local/bin/kapp \
    && chmod +x /usr/local/bin/kapp

LABEL name="node-awscli-kubectl-kapp"
LABEL version="0.0.1"
ENV PATH="./node_modules/.bin:${PATH}"