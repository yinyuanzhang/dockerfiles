# Build via docker:
# docker build --build-arg cores=8 -t blocknetdx/gbx:latest .

FROM ubuntu:xenial

ARG cores=1
ENV ecores=$cores

RUN apt update \
  && apt install -y --no-install-recommends \
     software-properties-common \
     ca-certificates \
     wget curl git python vim \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN add-apt-repository ppa:bitcoin/bitcoin \
  && apt update \
  && apt install -y --no-install-recommends \
     curl build-essential libtool autotools-dev automake \
     python3 bsdmainutils cmake libevent-dev autoconf automake \
     pkg-config libssl-dev libboost-system-dev libboost-filesystem-dev \
     libboost-chrono-dev libboost-program-options-dev libboost-test-dev \
     libboost-thread-dev libdb4.8-dev libdb4.8++-dev libgmp-dev \
     libminiupnpc-dev libzmq3-dev \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Build source
RUN mkdir -p /opt/gobyte \
  && mkdir -p /opt/blockchain/config \
  && mkdir -p /opt/blockchain/data \
  && ln -s /opt/blockchain/config /root/.gobyte \
  && cd /opt/gobyte \
  && mkdir gobyte \
  && git clone --depth 1 --branch v0.12.2.4 https://github.com/gobytecoin/gobyte gobyte \
  && cd /opt/gobyte/gobyte/ \
  && cd depends \
  && make -j$ecores NO_QT=1 \
  && cd .. \
  && chmod +x ./autogen.sh \
  && ./autogen.sh \
  && ./configure --with-gui=no --enable-hardening --prefix=`pwd`/depends/x86_64-pc-linux-gnu \
  && make -j$ecores \
  && cp /opt/gobyte/gobyte/src/gobyted /opt/blockchain/gobyted \
  && rm -rf /opt/gobyte/

# Write default gobyte.conf (can be overridden on commandline)
RUN echo "datadir=/opt/blockchain/data  \n\
                                        \n\
dbcache=256                             \n\
maxmempool=512                          \n\
port=12455                               \n\
rpcport=12454                          \n\
listen=1                                \n\
server=1                                \n\
logtimestamps=1                         \n\
logips=1                                \n\
rpcthreads=8                            \n\
rpcallowip=127.0.0.1                    \n\
rpctimeout=15                           \n\
rpcclienttimeout=15                     \n" > /opt/blockchain/config/gobyte.conf

WORKDIR /opt/blockchain/
VOLUME ["/opt/blockchain/config", "/opt/blockchain/data"]

# Port, RPC, Test Port, Test RPC
EXPOSE 12455 12454  18332  19332

CMD ["/opt/blockchain/gobyted", "-daemon=0"]