FROM ubuntu:bionic

RUN apt-get update \
    && apt-get -y upgrade \
	&& export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install libfontconfig1 libfreetype6 libx11-6 libx11-xcb1 libxcb1 wget \
	&& wget https://github.com/heptacoin/heptacoin/releases/download/v0.13.2/heptacoin-0.13.2-2ba515b-ubuntu-amd64.deb -O /tmp/wallet.deb \
	&& dpkg -i /tmp/wallet.deb

#rpc port & main port
EXPOSE 6666 9444

ENV HOME /data

COPY start.sh /start.sh
COPY gen_config.sh /gen_config.sh
RUN chmod 777 /*.sh
CMD /start.sh heptacoin.conf HEPTA heptacoind