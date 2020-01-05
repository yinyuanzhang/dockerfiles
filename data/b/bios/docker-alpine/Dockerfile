FROM alpine

RUN apk add --no-cache bash python3 python3-dev py3-pip openssh-client && \
    pip3 install --upgrade pip && \
    pip3 install awscli --upgrade --user && \
    ln -s /root/.local/bin/aws /usr/local/bin/aws && \
    rm -rf /var/cache/apk/*
