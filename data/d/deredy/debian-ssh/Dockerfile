FROM debian:stretch
LABEL maintainer="Eduard Baun <eduard@baun.de>"

RUN apt-get update && \
	apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \
	apt-get install -y openssh-client && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
