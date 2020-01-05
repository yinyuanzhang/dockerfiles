FROM chainmapper/walletbase-xenial
	
ENV WALLET_URL=https://github.com/aeriumcoin/AeriumX/releases/download/v2.2/AeriumX-2.2.0-x86_64-pc-linux-gnu.zip

RUN wget $WALLET_URL -O /tmp/wallet.zip \
	&& unzip /tmp/wallet.zip -d /usr/local/bin \
	&& chmod +x /usr/local/bin/*

#zmq, rpc & main port
EXPOSE 5555 6666 35407

RUN mkdir /data
ENV HOME /data

COPY start.sh /start.sh
COPY gen_config.sh /gen_config.sh
COPY wallet.sh /wallet.sh
RUN chmod 777 /*.sh
CMD /start.sh aeriumx.conf AEX aeriumxd