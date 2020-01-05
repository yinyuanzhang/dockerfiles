FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y ntp git build-essential libssl-dev libdb-dev libdb++-dev libboost-all-dev libqrencode-dev autoconf automake pkg-config unzip curl wget make bsdmainutils autotools-dev libtool libevent-dev libgmp-dev jq gnupg gosu && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:bitcoin/bitcoin && \
    apt-get update && \
    apt-get install -y libdb4.8-dev libdb4.8++-dev

# Install secp256k1
RUN cd /root && \
    git clone https://github.com/bitcoin/secp256k1.git && \
    cd secp256k1 && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install
