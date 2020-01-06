
FROM ubuntu:disco
MAINTAINER Seppe Stas <seppe@productize.be>
LABEL Description="Minimal KiCad image based on Ubuntu"

ADD kicad-ppa.pgp .
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
	apt-get -y update && \
	apt-get -y install gnupg2 && \
	echo 'deb http://ppa.launchpad.net/js-reynaud/kicad-5.1/ubuntu disco main' >> /etc/apt/sources.list && \
	apt-key add kicad-ppa.pgp && \
	apt-get -y update && apt-get -y install --no-install-recommends kicad && \
	apt-get -y purge gnupg2 && \
	apt-get -y autoremove && \
	rm -rf /var/lib/apt/lists/* && \
	rm kicad-ppa.pgp
