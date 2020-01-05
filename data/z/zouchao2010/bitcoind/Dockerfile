FROM zouchao2010/python:2.7

VOLUME /var/lib/bitcoind

ADD . /opt/bitcoind
WORKDIR /opt/bitcoind
RUN cp -r testnet /var/lib/bitcoind
RUN cp -r livenet /var/lib/bitcoind

ENV TESTNET 0
ENV VERSION 0.13.1

#更改源
#RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
#RUN cp sources.list /etc/apt/
RUN apt-get update \
    && apt-get install -y wget \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && apt-get autoclean -y \
    && rm -rf /var/lib/apt/lists/*

#安装bitcoind
RUN wget https://bitcoin.org/bin/bitcoin-core-$VERSION/bitcoin-$VERSION-x86_64-linux-gnu.tar.gz   \
    && tar zxvf bitcoin-$VERSION-x86_64-linux-gnu.tar.gz \
    && ln -sfv /opt/bitcoind/bitcoin-$VERSION/bin/* /usr/local/bin \
    && rm -rf bitcoin-$VERSION-linux64.tar.gz

RUN chmod 755 run.sh

#Livenet
EXPOSE 8332
EXPOSE 8333
EXPOSE 8334

#Testnet
EXPOSE 18332
EXPOSE 18333
EXPOSE 18334

CMD ["./run.sh"]
