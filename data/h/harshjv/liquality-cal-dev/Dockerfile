FROM ubuntu:18.04

ENV BITCOIN_VERSION=0.16.1
ENV PARITY_VERSION=1.11.7
ENV NVM_VERSION=0.33.11

WORKDIR /liquality

RUN mkdir -p /liquality/bin \
             /liquality/bitcoin/data \
             /liquality/ethereum/data

ENV PATH="/liquality/bin:${PATH}"

RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates curl tar libssl1.0.0 libusb-1.0-0 libusb-1.0-0-dev libudev-dev git-core python build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN curl -O \
    https://bitcoin.org/bin/bitcoin-core-${BITCOIN_VERSION}/bitcoin-${BITCOIN_VERSION}-x86_64-linux-gnu.tar.gz && \
    tar -xzf bitcoin-${BITCOIN_VERSION}-x86_64-linux-gnu.tar.gz && \
    cp bitcoin-${BITCOIN_VERSION}/bin/* /liquality/bin && \
    rm -rf bitcoin-${BITCOIN_VERSION} bitcoin-${BITCOIN_VERSION}-x86_64-linux-gnu.tar.gz

RUN curl -O \
    https://releases.parity.io/v${PARITY_VERSION}/x86_64-unknown-linux-gnu/parity_${PARITY_VERSION}_ubuntu_amd64.deb && \
    dpkg -i parity_${PARITY_VERSION}_ubuntu_amd64.deb && \
    apt-get install -f && \
    rm -rf parity_${PARITY_VERSION}_ubuntu_amd64.deb

COPY bitcoin.conf /liquality/bitcoin/bitcoin.conf

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v${NVM_VERSION}/install.sh | bash

RUN echo '#!/bin/bash\nbitcoind -conf=/liquality/bitcoin/bitcoin.conf -daemon=1' > /liquality/bin/bitcoind-daemon && \
    chmod +x /liquality/bin/bitcoind-daemon

RUN echo '#!/bin/bash\nparity --chain=dev --db-path=/liquality/ethereum/data daemon /liquality/ethereum/parity.pid' > /liquality/bin/parity-daemon && \
    chmod +x /liquality/bin/parity-daemon

EXPOSE 18332 8080 8545 8180
VOLUME /liquality
