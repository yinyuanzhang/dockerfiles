FROM debian:9.1
ENV DEBIAN_FRONTEND noninteractive

ENV ASTERISK_VERSION 15.1.0-rc1

RUN \

	#upgrade

	apt-get update &&\
	apt-get dist-upgrade -y &&\

	# common

	apt-get install -y \
		build-essential \
		curl \
	&&\

	# asterisk

	apt-get install -y \
		libncurses5-dev \
		uuid-dev \
		libjansson4 libjansson-dev \
		xmlstarlet libxml2-dev libxslt1-dev \
		libsqlite3-dev \
		libssl-dev \
		libcurl3 libcurl4-openssl-dev \
		zlib1g-dev \
		libsrtp2-1 libsrtp2-dev \
	&&\
	cd /usr/src &&\
	curl http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-$ASTERISK_VERSION.tar.gz | tar zxf - &&\
	cd asterisk-$ASTERISK_VERSION &&\

	# ast_mongo

#	apt-get install -y \
#		libbson-dev \
#		libmongoc-dev \
#		autoconf \
#		automake \
#		pkg-config \
#	&&\
#	curl https://raw.githubusercontent.com/minoruta/ast_mongo/master/patches/ast_mongo-15.0.0.patch | sed 's~/local/~/~' | patch -p1 &&\
#	./bootstrap.sh &&\
#	apt-get purge --auto-remove -y \
#		autoconf \
#		automake \
#		pkg-config \
#	&&\

	# configure

	./configure &&\
	make menuselect.makeopts &&\
	menuselect/menuselect menuselect.makeopts \
		--disable BUILD_NATIVE \
		--disable CORE-SOUNDS-EN-GSM \
		--enable CORE-SOUNDS-RU-ULAW \
		--enable codec_opus \
	&&\

	# mp3

#	apt-get install -y subversion &&\
#	contrib/scripts/get_mp3_source.sh &&\
#	menuselect/menuselect menuselect.makeopts --enable format_mp3 &&\
#	apt-get purge --auto-remove -y subversion &&\

	# make & install

	make &&\
	make install &&\
	cp contrib/scripts/ast_tls_cert /usr/sbin &&\

	# cleanup

    cd .. &&\
	rm -rf asterisk-$ASTERISK_VERSION &&\
	rm /tmp/* &&\
	apt-get purge --auto-remove -y \
		build-essential \
		curl \
		libncurses5-dev \
		uuid-dev \
		libjansson-dev \
		libxml2-dev libxslt1-dev \
		libsqlite3-dev \
		libssl-dev \
		libcurl4-openssl-dev \
		zlib1g-dev \
		libsrtp2-dev \
	&&\
	apt-get clean &&\
	rm -rf /var/lib/apt/lists/*
