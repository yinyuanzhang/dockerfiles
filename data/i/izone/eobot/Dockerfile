FROM ubuntu:xenial
MAINTAINER Leonardo Loures <luvres@hotmail.com>

ENV \
	ALGORITHM="x11" \
	POOL="x11.eobot.com" \
	PORT="5555" \
	USERPASS="eobot.1777741:x" 

RUN \
	apt-get update \
	&& apt-get install -y libcurl3-gnutls

COPY minerd /usr/bin

CMD minerd -a $ALGORITHM -o stratum+tcp://$POOL:$PORT --userpass $USERPASS



