FROM chainmapper/walletbase-xenial

ENV WALLET_URL=https://github.com/seduscoin/seduscoin/releases/download/v1.0/seduscoin-cli-linux.tar.gz

RUN wget $WALLET_URL -O /tmp/wallet.tar.gz \
	&& cd /usr/local/bin \
	&& tar xvzf /tmp/wallet.tar.gz \
	&& rm /tmp/wallet.tar.gz

RUN mkdir /data
ENV HOME /data

#rpc port & main port
EXPOSE 6666

COPY start.sh /start.sh
COPY gen_config.sh /gen_config.sh
RUN chmod 777 /*.sh
CMD /start.sh sedus.conf SEDUS sedusd