FROM chainmapper/walletbase-xenial

RUN wget https://github.com/anucore/anucore/releases/download/daemon-1.2.0/AnuCoind -O /usr/local/bin/AnuCoind \
	&& chmod 777 /usr/local/bin/AnuCoind \
	&& mkdir -p /data

#rpc port & main port
EXPOSE 36964 36963

ENV HOME /data

COPY start.sh /start.sh
COPY gen_config.sh /gen_config.sh
RUN chmod 777 /*.sh
CMD /start.sh AnuCoin.conf ANU AnuCoind