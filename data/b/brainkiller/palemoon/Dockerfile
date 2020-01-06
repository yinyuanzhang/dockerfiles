FROM debian:testing

ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

RUN apt-get update \
	&& apt-get -y install gnupg wget \
	&& echo 'deb http://download.opensuse.org/repositories/home:/stevenpusser/Debian_Testing/ /' > /etc/apt/sources.list.d/home:stevenpusser.list \
	&& sed -e 's/deb/deb-src/' /etc/apt/sources.list > /etc/apt/sources.list.d/debian-sources.list \
	&& wget -q -O /tmp/palemoon.gpg 'http://download.opensuse.org/repositories/home:/stevenpusser/Debian_Testing/Release.key' \
	&& cat /tmp/palemoon.gpg \
	&& apt-key add /tmp/palemoon.gpg \
	&& apt-get update \
	&& apt-get install -y palemoon icedtea-plugin \
	&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*

CMD /usr/bin/palemoon
