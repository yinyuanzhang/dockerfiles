FROM ubuntu:bionic
LABEL MAINTAINER="Nelson Chen <crazysim@gmail.com>"

ARG DEBIAN_FRONTEND=noninteractive

RUN set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends wget aria2 ca-certificates curl git jq qemu-kvm qemu-utils unzip \
    \
    && PACKER_LATEST_VERSION=$(curl -s https://checkpoint-api.hashicorp.com/v1/check/packer | jq -r -M '.current_version') \
    && curl https://releases.hashicorp.com/packer/${PACKER_LATEST_VERSION}/packer_${PACKER_LATEST_VERSION}_linux_amd64.zip --output /tmp/packer_linux_amd64.zip \
    && unzip /tmp/packer_linux_amd64.zip -d /usr/local/bin/ \
    && rm -f /tmp/packer_linux_amd64.zip \
    \
    && apt purge -y curl git jq unzip \
    && rm -Rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean
