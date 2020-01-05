# Docker Adyax
#
#

FROM debian:stable

MAINTAINER Benoît GRUNENBERGER <bgrunenberger@adyax.com>

ENV DEBIAN_FRONTEND noninteractive


RUN echo 'vm.overcommit_memory = 1' > /etc/sysctl.conf && \
	apt-get update -y && \
	apt-get install -y redis-server && \
	apt-get -y -q autoclean && \
	apt-get -y -q autoremove


EXPOSE 6379

ENTRYPOINT ["redis-server"]

#CMD ["service redis-server start"]
