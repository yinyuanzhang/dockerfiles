FROM chainmapper/walletbase-xenial

ENV WALLET_URL=https://github.com/Seather/Seather/releases/download/v1.0.0/linux64.tar.gz

RUN wget $WALLET_URL -O /tmp/wallet.tar.gz \
	&& cd /usr/local/bin \
	&& tar xvzf /tmp/wallet.tar.gz --strip-components 1\
	&& rm /tmp/wallet.tar.gz

RUN mkdir /data
ENV HOME /data

#rpc port & main port
EXPOSE 22501 22500

COPY start.sh /start.sh
COPY gen_config.sh /gen_config.sh
RUN chmod 777 /*.sh
CMD /start.sh seather.conf STR seatherd