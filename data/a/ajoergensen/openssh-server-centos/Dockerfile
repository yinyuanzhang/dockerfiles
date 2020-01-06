FROM ajoergensen/baseimage-centos
MAINTAINER ajoergensen

COPY root/ /

RUN \
	/build/setup.sh && \
	rm -rf /build

EXPOSE 22

VOLUME /config /etc/ssh/keys
