FROM ubuntu:16.04

# Install necessary packages
RUN apt-get update && apt-get --assume-yes install git
RUN apt-get --assume-yes install build-essential libtool autotools-dev autoconf pkg-config libssl-dev
RUN apt-get --assume-yes install libboost-all-dev
RUN apt-get --assume-yes install software-properties-common
RUN add-apt-repository ppa:bitcoin/bitcoin
RUN apt-get update
RUN apt-get --assume-yes install libdb4.8-dev libdb4.8++-dev
RUN apt-get --assume-yes install libminiupnpc-dev
RUN apt-get --assume-yes install libevent-dev
RUN apt-get --assume-yes install curl

# Clone git repository
RUN git clone https://github.com/securecloudnet/SecureCloud.git wallet

WORKDIR /wallet

# Build wallet from source
RUN ./autogen.sh
RUN ./configure --disable-tests --without-gui
RUN make

# Copy conf file
COPY ./wallet.conf /root/.securecloud/securecloud.conf

HEALTHCHECK --interval=120s --timeout=30s --start-period=60s --retries=3 CMD curl --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"getinfo","params":[]}' -H 'content-type:text/plain;' http://nodevault:password@127.0.0.1:8000/ || exit 1

# Expose port 8000 for RPC
EXPOSE 8000

WORKDIR /wallet/src

CMD /wallet/src/securecloudd -prune=550 -rest -reindex && sleep infinity