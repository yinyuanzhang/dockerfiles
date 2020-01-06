FROM chainmapper/walletbase-xenial
	
ENV WALLET_URL=https://github.com/papelcoin/papelcoin/releases/download/1.0.0.4/Papel.Core.Linux.zip

RUN wget $WALLET_URL -O /tmp/wallet.zip \
	&& unzip /tmp/wallet.zip -d /usr/local/bin \
	&& chmod +x /usr/local/bin/*

#rpc port & main port
EXPOSE 6666 21999

RUN mkdir /data
ENV HOME /data

COPY start.sh /start.sh
COPY gen_config.sh /gen_config.sh
COPY wallet.sh /wallet.sh
RUN chmod 777 /*.sh
CMD /start.sh papel.conf PAPEL papeld