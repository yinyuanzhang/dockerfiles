FROM ubuntu:16.04
MAINTAINER Sreekanth G S <mail@sreekanth.in>

ARG BITCOIN_VERSION

WORKDIR /root
RUN apt update
RUN apt-get install -y wget
RUN wget https://bitcoin.org/bin/bitcoin-core-0.16.0/bitcoin-0.16.0-x86_64-linux-gnu.tar.gz 
RUN tar -zvxf bitcoin-0.16.0-x86_64-linux-gnu.tar.gz
RUN ls
RUN mv bitcoin-0.16.0 bitcoincore
RUN cp bitcoincore/bin/* /usr/local/bin
RUN bitcoind --help

VOLUME ["/opt/bitcoin"]

EXPOSE 8332
EXPOSE 8333
EXPOSE 18332
EXPOSE 18333

CMD ["bitcoind", "--conf=/opt/bitcoin/bitcoind.conf", "--printtoconsole"]