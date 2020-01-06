FROM node:8-alpine

RUN mkdir -p /zos
WORKDIR /zos

RUN apk update \
    && apk add --no-cache \
        build-base \
        gcc \
        git \
        bash \
        openssh \
        python \
        tmux \
        jq

RUN npm install --unsafe-perm --global @openzeppelin/cli ganache-cli web3 truffle-privatekey-provider

ENTRYPOINT ["/bin/bash"]
