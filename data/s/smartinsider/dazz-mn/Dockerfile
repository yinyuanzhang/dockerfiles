FROM ubuntu:xenial
MAINTAINER Smart Insider <smartyinsider@gmail.com>

RUN apt-get update --yes && apt-get install --yes \
        build-essential libtool autotools-dev autoconf pkg-config libssl-dev libboost-all-dev libevent-dev wget \
        software-properties-common && \
    add-apt-repository --yes ppa:bitcoin/bitcoin && \
        apt-get update

RUN apt-get install --yes libdb4.8-dev libdb4.8++-dev \
            libminiupnpc-dev libzmq3-dev && \
    apt-get clean && \
    rm -rf /var/lib/ap/lists/*

#ARGS
ARG COIN_NAME=dazzling
ARG TARDAEMON=dazz-ubuntu-16.tar.gz
ARG TARDB=database.tar.gz
ARG GIT=https://cryptoyen.icu/wallet/dazz/

ENV port=29850
ENV mnprivkey=xxxxxxxxxxxxxxxxxx
ENV ip==x.x.x.x

#DAEMON INSTALL
WORKDIR /usr/local/bin
RUN wget -O ${TARDAEMON} ${GIT}${TARDAEMON} && tar -xzf ${TARDAEMON} && rm ${TARDAEMON}

#DB INSTALL
WORKDIR /root/.${COIN_NAME}
RUN wget -O ${TARDB} ${GIT}${TARDB} && tar -xzf ${TARDB} && rm ${TARDB}

WORKDIR /root

ENTRYPOINT dazzlingd --port=$port --masternodeprivkey=$mnprivkey --rpcuser=rpc_user --rpcpassword=rpc_pwassword --masternodeaddr=$ip --printtoconsole --masternode=1 --txindex=1 --bantime=50 --maxconnections=256



 






