FROM debian:jessie

ENV BITCOIND_P2P_HOST 127.0.0.1
ENV BITCOIND_P2P_PORT 8333

RUN apt-get update \
    && apt-get install -y wget unzip make yasm g++ vim\
    && apt-get autoremove -y \
    && apt-get clean -y \
    && apt-get autoclean -y \
    && rm -rf /var/lib/apt/lists/*

RUN cd /opt \
    && wget https://github.com/TheBlueMatt/RelayNode/archive/master.zip \
    && unzip master.zip \
    && mv RelayNode-master RelayNode \
    && cd RelayNode/c++ \
    && make

CMD ["sh", "-c", "start-stop-daemon --start --exec /opt/RelayNode/c++/relaynetworkclient -- $BITCOIND_P2P_HOST $BITCOIND_P2P_PORT"]


