FROM chainmapper/walletbase-bionic
	
ENV WALLET_URL=https://github.com/avymantech/lobstex/releases/download/v2.4.0/lobstex-2.4.0-linux64.tar.gz

RUN wget $WALLET_URL -O /tmp/wallet.tar.gz \
	&& cd /usr/local/bin \
	&& tar zxvf /tmp/wallet.tar.gz

#rpc port & main port & zmqport
EXPOSE 6666 14146 5555

RUN mkdir /data
ENV HOME /data

COPY start.sh /start.sh
COPY gen_config.sh /gen_config.sh
COPY wallet.sh /wallet.sh
RUN chmod 777 /*.sh
CMD /start.sh lobstex.conf LOBS lobstexd