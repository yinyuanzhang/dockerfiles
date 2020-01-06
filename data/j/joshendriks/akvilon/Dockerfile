FROM joshendriks/walletbase

RUN apt-get update \
    && apt-get -y upgrade \
	&& apt-get -y install libminiupnpc-dev libminiupnpc-dev
	
	
ENV GIT_COIN_URL    https://github.com/Akviloncoin/Akvilon.git
ENV GIT_COIN_NAME   akvilon   

RUN	git clone $GIT_COIN_URL $GIT_COIN_NAME \
	&& cd $GIT_COIN_NAME \
	&& chmod +x share/genbuild.sh \
	&& chmod +x src/leveldb/build_detect_platform \
	&& cd src \
	&& make -f	makefile.unix RELEASE=1\
	&& cp akviloncoind /usr/local/bin \
	&& cd / && rm -rf /$GIT_COIN_NAME \
	&& mkdir /data \
	&& mkdir /data/.AkvilonCoin
	
#Add a config so you can run without providing a AkvilonCoin.conf through a volume
COPY AkvilonCoin.conf /data/.AkvilonCoin/AkvilonCoin.conf

#rpc and p2p port
EXPOSE 49086 49085

ENV HOME /data

COPY start.sh /start.sh
RUN chmod 777 /start.sh
CMD /start.sh