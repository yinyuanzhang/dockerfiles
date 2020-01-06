FROM joshendriks/walletbase

ENV GIT_COIN_URL    https://github.com/AegeusCoin/aegeus.git
ENV GIT_COIN_NAME   aegeus    

RUN	git clone $GIT_COIN_URL $GIT_COIN_NAME \
	&& cd $GIT_COIN_NAME \
	&& ./autogen.sh && ./configure && make && make install \
	&& mkdir -p /data/.aegeus
	
#Add a config so you can run without providing a aegeus.conf through a volume
COPY aegeus.conf /data/.aegeus/aegeus.conf

#rpc and masternode port
EXPOSE 29329 29328

ENV HOME /data

COPY start.sh /start.sh
RUN chmod 777 /start.sh
CMD /start.sh