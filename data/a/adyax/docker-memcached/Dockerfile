# Docker Adyax
#
#

FROM debian:stable

MAINTAINER Benoît GRUNENBERGER <bgrunenberger@adyax.com>


RUN apt-get update -y && \
	apt-get install -y memcached && \
	apt-get -y autoclean && \
	apt-get -y autoremove


EXPOSE 11211
USER daemon
ENTRYPOINT ["memcached"]

#CMD ["service", "memcached", "start", "&"]
