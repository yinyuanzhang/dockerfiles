FROM linuxserver/deluge:latest

RUN \
 echo "**** Install CURL ****" && \
 apt-get install -y \
	curl && \
 echo "**** cleanup ****" && \
 apt-get --purge autoremove -y && \
 apt-get clean && \
 rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/*
