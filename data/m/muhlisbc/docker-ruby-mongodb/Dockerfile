FROM muhlisbc/docker-ruby

MAINTAINER Muhlis BC "muhlisbc@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0C49F3730359A14518585931BC711F9BA15703C6 \
	&& echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y mongodb-org \
	&& mkdir -p /data/db /data/configdb \
	&& chown -R mongodb:mongodb /data/db /data/configdb \
	&& rm -rf /var/lib/apt/lists/* /tmp/*
