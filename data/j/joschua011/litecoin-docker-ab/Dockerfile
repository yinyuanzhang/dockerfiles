FROM ubuntu:16.04
MAINTAINER Johann Tanzer <mail@johanntanzer.at>

WORKDIR /root

RUN apt-get update && apt-get install -y wget && \
    wget https://download.litecoin.org/litecoin-0.13.2/linux/litecoin-0.13.2-x86_64-linux-gnu.tar.gz && \
    tar -zvxf litecoin-0.13.2-x86_64-linux-gnu.tar.gz && \
    mv litecoin-0.13.2 litecoin

VOLUME ["/opt/litecoin"]

EXPOSE 9332

CMD ["/root/litecoin/bin/litecoind", "--conf=/opt/litecoin/litecoind.conf", "--printtoconsole"]
