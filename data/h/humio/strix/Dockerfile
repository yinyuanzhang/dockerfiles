FROM alpine:latest

ENV HUMIOCTL_VERSION 0.23.0
ENV KUBECTL_VERSION 1.14.3

RUN apk update && apk upgrade && apk add bash curl jq python

# Temporarily using custom humioctl until I can get access to snapcraft so I can publish a new humioctl binary (jswoods)
# RUN wget -O /tmp/humioctl.tar.gz https://github.com/humio/cli/releases/download/v${HUMIOCTL_VERSION}/humioctl_${HUMIOCTL_VERSION}_Linux_64-bit.tar.gz && \
#   cd /tmp && tar zxvf /tmp/humioctl.tar.gz && cp ./humioctl /usr/local/bin/humioctl && cd - && rm -rf /tmp/* && chmod +x /usr/local/bin/humioctl
COPY ./humioctl /usr/local/bin/humioctl
RUN chmod +x /usr/local/bin/humioctl

RUN wget -O /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl && chmod +x /usr/local/bin/kubectl

# Install Google Cloud SDK
RUN curl https://sdk.cloud.google.com | bash

# Install Microsoft Azure CLI
#RUN apk add py-pip gcc python-dev libffi-dev musl-dev openssl-dev make && \
#    pip --no-cache-dir install azure-cli

COPY scripts/* /
RUN chmod +x /*.sh
