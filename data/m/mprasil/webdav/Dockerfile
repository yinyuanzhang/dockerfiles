# VERSION 0.1
# AUTHOR:         Miroslav Prasil <miroslav@prasil.info>
# DESCRIPTION:    lighttpd configured as WebDAV

FROM ubuntu:14.04
MAINTAINER Miroslav Prasil <miroslav@prasil.info>

ENV LAST_REFRESHED 29. September 2014
# Update & install packages
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y  install lighttpd \
	lighttpd-mod-webdav

RUN mkdir -p /site/input

ADD htpasswd /site/
ADD share.conf /etc/lighttpd/conf-available/20-share.conf

RUN lighty-enable-mod auth webdav share
RUN mkdir -p /var/run/lighttpd && chown www-data.www-data /var/run/lighttpd /site/input

EXPOSE 80
VOLUME /site/input/

ENTRYPOINT ["/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]

