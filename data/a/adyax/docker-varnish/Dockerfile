# Docker Adyax
#
#

FROM debian:wheezy

MAINTAINER Benoît GRUNENBERGER <bgrunenberger@adyax.com>

ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update -y && \
    apt-get install -y curl apt-transport-https python-software-properties && \
    apt-get update -y && \
    curl https://repo.varnish-cache.org/debian/GPG-key.txt | apt-key add - && \
	echo "deb https://repo.varnish-cache.org/debian/ wheezy varnish-4.0" >> /etc/apt/sources.list.d/varnish-cache.list && \
	apt-get update -y && \
	apt-get install -y varnish && \
	apt-get -yq autoclean && \
	apt-get -yq autoremove

ADD default.vcl /etc/varnish/default.vcl

EXPOSE 6081 6082

ENTRYPOINT ["varnish"]

#CMD ["service varnish start"]
