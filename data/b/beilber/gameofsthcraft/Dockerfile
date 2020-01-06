# -----------------------------------------------------------------------------
# docker-gameofsthcraft
#
# A dockerized minecraft server for the gameofsthcraft modpack
#
# Needs work, comments and serious polish
#
# Authors: Brian Eilber
# Updated: March 22nd, 2015
# Require: Docker (http://www.docker.io/)
# -----------------------------------------------------------------------------


FROM	ubuntu:14.04

MAINTAINER Brian Eilber <brian.eilber@gmail.com>

ENV	DEBIAN_FRONTEND noninteractive

RUN	apt-get --yes update; apt-get --yes upgrade; apt-get --yes install software-properties-common
RUN	sudo apt-add-repository --yes ppa:webupd8team/java; apt-get --yes update
RUN	echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections  && \
	echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections  && \
	apt-get --yes install curl oracle-java7-installer unzip && \
	apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN	mkdir /server
RUN	wget http://files.spankythehero.com/gameofsthcraft-qa.115-server.zip -O /server/pack.zip
RUN	cd /server && unzip pack.zip && rm pack.zip
RUN	cd /server && sh install.sh

RUN     echo "eula=true" > /server/eula.txt
RUN	chmod +x /server/start.sh


EXPOSE	25565
EXPOSE	8123

VOLUME	["/data"]

CMD	["/server/start.sh"]
