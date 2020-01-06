# locking release to 5b398f77-ls22 due to some error with current builds
FROM linuxserver/deluge:5b398f77-ls22

# install software
RUN \
 echo "**** install packages ****" && \
 apt-get update && \
 apt-get install -y apt-utils iputils-ping && \
 echo "**** cleanup ****" && \
 apt-get --purge autoremove -y && \
 apt-get clean && \
 rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/*
