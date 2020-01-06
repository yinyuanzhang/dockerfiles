FROM gcc:4

# Build docs:
# https://github.com/bitcoin/bitcoin/blob/master/doc/build-unix.md

ADD . /src/
WORKDIR /src/

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install \
      bsdmainutils \
      libboost-filesystem-dev \
      libboost-program-options-dev \
      libboost-system-dev \
      libboost-test-dev \
      libboost-thread-dev \
      libdb-dev \
      libdb++-dev \
      libevent-dev \
      libminiupnpc-dev \
      libssl-dev \
      libzmq3-dev \
  && \
  ./autogen.sh && \
  ./configure --help && \
  ./configure --without-gui --enable-miniupnpc --enable-zmq --with-incompatible-bdb \
  && \
  make && \
  make install && \
  make clean \
  && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y purge bsdmainutils \
  && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y autoremove --purge \
  && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y purge '^lib.*-dev$' \
  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/

ENTRYPOINT [ "bitcoind", "-printtoconsole", "-logtimestamps=0" ]
