# Docker Adyax
#
#

FROM debian:wheezy

MAINTAINER Benoît GRUNENBERGER <bgrunenberger@adyax.com>

ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update -y && \
	apt-get install -y python-software-properties && \
	apt-get update -y && \
	apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db && \
	add-apt-repository 'deb http://ftp.igh.cnrs.fr/pub/mariadb/repo/10.0/debian wheezy main' && \
	apt-get update -y && \
	apt-get install -y mariadb-server mariadb-client && \
	apt-get -y -q autoclean && \
	apt-get -y -q autoremove

EXPOSE 3306

ENTRYPOINT ["mysql"]

#CMD ["service mysql start"]
