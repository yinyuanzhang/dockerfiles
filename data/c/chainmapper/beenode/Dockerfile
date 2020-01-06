FROM chainmapper/walletbase-bionic

ENV WALLET_URL=https://github.com/bee-group/beenode/releases/download/v0.7.1/beenodecore-0.7.1-linux64.tar.gz

RUN wget $WALLET_URL -O /tmp/wallet.tar.gz \
	&& cd /usr/local/bin \
	&& tar zxvf /tmp/wallet.tar.gz  --strip-components 2\
	&& mkdir -p /data/.beenode

#rpc port & main port & zmqport
EXPOSE 6666 4244 5555

ENV HOME /data

COPY start.sh /start.sh
COPY gen_config.sh /gen_config.sh
COPY wallet.sh /wallet.sh
RUN chmod 777 /*.sh
CMD /start.sh beenode.conf BNODE beenoded