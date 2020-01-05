FROM ubuntu:xenial

ENV GIT_COIN_URL    https://github.com/muecoin/MUE.git
ENV GIT_COIN_NAME   monetaryunit

RUN	apt-get -qq update \
	&& apt-get -y install software-properties-common \
	&& add-apt-repository -yu ppa:bitcoin/bitcoin \
    && apt-get -y install build-essential \
    libcurl4-gnutls-dev protobuf-compiler libboost-all-dev autotools-dev automake \
    libboost-all-dev libssl-dev make autoconf libtool git apt-utils g++ \
    libprotobuf-dev pkg-config libudev-dev libqrencode-dev bsdmainutils \
    pkg-config libgmp3-dev libevent-dev jp2a pv virtualenv libdb4.8-dev libdb4.8++-dev

	
RUN	git clone $GIT_COIN_URL $GIT_COIN_NAME \
	&& cd $GIT_COIN_NAME \	
	&& git checkout tags/v2.1.3 \
	&& chmod +x autogen.sh \
	&& chmod +x share/genbuild.sh \
	&& chmod +x src/leveldb/build_detect_platform \
	&& ./autogen.sh && ./configure --with-libressl --disable-dependency-tracking --enable-tests=no --without-gui --without-miniupnpc\
	&& make \
	&& make install

RUN mkdir /data
ENV HOME /data

#rpc port & main port
EXPOSE 6666 19687

COPY start.sh /start.sh
COPY gen_config.sh /gen_config.sh
COPY wallet.sh /wallet.sh
RUN chmod 777 /*.sh
CMD /start.sh monetaryunit.conf MUE monetaryunitd