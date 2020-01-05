FROM ruby:2.4-alpine

RUN \
        apk add --no-cache \
                cmake \
                curl \
                gcc \
                git \
                jq \
                libc-dev \
                make \
                openssh \
                python3 \
                wget \
                zip \
        && apk add --no-cache --virtual .builddeps \
                unzip \
                python3-dev \
        && pip3 install --no-cache-dir \
                awscli==1.11.183 \
        && cd /tmp \
                && wget https://releases.hashicorp.com/packer/1.1.1/packer_1.1.1_linux_amd64.zip \
                && unzip *.zip \
                && install -t /usr/bin -g root -o root -m 0755 /tmp/packer* \
                && rm -f /tmp/*.zip /tmp/packer* \
        && apk del .builddeps
