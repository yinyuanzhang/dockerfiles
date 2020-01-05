############################################################
# Dockerfile to build supervisor container image
# based on Ubuntu Trusty
############################################################
# Container APP für EPGD mit Frodo Yavdr Scripten
############################################################

# Set the base Image
FROM derbrummbaer/im-base-phusion1804:latest

# File Author / Maintainer
MAINTAINER Sven Berger

############################################################
# RUN INSTALL AS root
############################################################

USER root

############################################################
# Environment Variables
############################################################

ENV LC_ALL de_DE.UTF-8
ENV LANG de_DE.UTF-8
ENV LANGUAGE de_DE.UTF-8
ENV USERNAME vdr
ENV USERID 666
ENV GROUPID 666
ENV TZ Europe/Berlin

############################################################
# Container Users
############################################################

RUN groupmod -n $USERNAME users
RUN adduser --uid $USERID --gid 100 --disabled-login --no-create-home --disabled-password vdr

############################################################
# Add Software Repositories
############################################################

RUN apt-get update; \
	apt-get install software-properties-common -y; \
	apt-add-repository ppa:yavdr/experimental-main -y
#	apt-add-repository ppa:yavdr/main -y; \
#	apt-add-repository ppa:frodo-vdr/stable-vdr; \
RUN apt-get update; \
	apt-get dist-upgrade -y

############################################################
# Begin Installation
############################################################

RUN apt-get install vdr-epg-daemon -y
#   rm nicht benötigt bei 18.04
#	rm /etc/init.d/epgd

############################################################
# Verzeichnisse anlegen
############################################################

RUN mkdir -p /var/cache/epgd/epgdata; \
	mkdir -p /var/cache/epgd/tvsp; \
	mkdir -p /var/cache/epgd/tvm; \
	mkdir -p /var/cache/vdr/epgimages

############################################################
# Backup installed Config
############################################################

# copy /etc/epgd /backup/etc/epgd
RUN mkdir -p /backup/etc/epgd && cp -a /etc/epgd/* /backup/etc/epgd

# copy /var/epgd/www/channellogos /backup/var/epgd/www/channellogos
RUN mkdir -p /backup/var/epgd/www && cp -a /var/epgd/www/* /backup/var/epgd/www

# copy /var/cache/epgd /backup/var/cache/epgd
RUN mkdir -p /backup/var/cache/epgd && cp -a /var/cache/epgd/* /backup/var/cache/epgd

############################################################
# Copy Files
############################################################

ADD scripte/start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh
ADD scripte/install.sh /usr/local/bin/install.sh
RUN chmod +x /usr/local/bin/install.sh

ADD scripte/startepgd.sh /usr/local/bin/startepgd.sh
RUN chmod +x /usr/local/bin/startepgd.sh
ADD scripte/startepghttpd.sh /usr/local/bin/startepghttpd.sh
RUN chmod +x /usr/local/bin/startepghttpd.sh

RUN mkdir /etc/service/epgd

ADD scripte/runepgd.sh /etc/service/epgd/run
RUN chmod +x /etc/service/epgd/run
RUN mkdir /etc/service/epghttpd
ADD scripte/runepghttpd.sh /etc/service/epghttpd/run
RUN chmod +x /etc/service/epghttpd/run

############################################################
# Remove Apt Data
############################################################

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

############################################################
# Container RUN USER
############################################################

#USER $USERNAME

############################################################
# Ports needed
############################################################

############################################################
# Ports needed by App
############################################################

EXPOSE 8888
EXPOSE 9999

############################################################
# Folders needed
############################################################

VOLUME /etc/epgd
VOLUME /var/cache/epgd
VOLUME /var/epgd/www/channellogos

############################################################
# Container Start
############################################################
#ENTRYPOINT ["/sbin/my_init"]

ENTRYPOINT ["/usr/local/bin/start.sh"]
