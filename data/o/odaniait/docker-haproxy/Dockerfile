FROM odaniait/docker-base:latest
MAINTAINER Mike Petersen <mike@odania-it.de>

RUN apt-get update && apt-get install -y libssl1.0.0 libpcre3 --no-install-recommends

ENV HAPROXY_MAJOR 1.6
ENV HAPROXY_VERSION 1.6.1
ENV HAPROXY_MD5 7343def2af8556ebc8972a9748176094

# see http://sources.debian.net/src/haproxy/1.5.8-1/debian/rules/ for some helpful navigation of the possible "make" arguments
RUN set -x && apt-get update && apt-get install -y curl gcc libc6-dev libpcre3-dev libssl-dev make
RUN buildDeps='curl gcc libc6-dev libpcre3-dev libssl-dev make' \
	&& set -x \
	&& curl -SL "http://www.haproxy.org/download/${HAPROXY_MAJOR}/src/haproxy-${HAPROXY_VERSION}.tar.gz" -o haproxy.tar.gz \
	&& echo "${HAPROXY_MD5}  haproxy.tar.gz" | md5sum -c \
	&& mkdir -p /usr/src/haproxy \
	&& tar -xzf haproxy.tar.gz -C /usr/src/haproxy --strip-components=1 \
	&& rm haproxy.tar.gz \
	&& make -C /usr/src/haproxy \
		TARGET=linux2628 \
		USE_PCRE=1 PCREDIR= \
		USE_OPENSSL=1 \
		USE_ZLIB=1 \
		all \
		install-bin \
	&& mkdir -p /usr/local/etc/haproxy \
	&& cp -R /usr/src/haproxy/examples/errorfiles /usr/local/etc/haproxy/errors \
	&& rm -rf /usr/src/haproxy

# Setup haproxy with supervisord
RUN mkdir -p /etc/service/haproxy
COPY runit/haproxy.sh /etc/service/haproxy/run
RUN ln -s /usr/local/etc/haproxy/ /etc/haproxy

RUN groupadd haproxy
RUN useradd -g haproxy -r haproxy

EXPOSE 80 1936

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
