ARG TAG=fpm
FROM php:${TAG}
ARG VERSION=master
LABEL maintainer="Brutus <brutus.dmc@googlemail.com>"
RUN set -ex \
	&& URL="https://github.com/phalcon/cphalcon/archive/${VERSION}.tar.gz" \
	&& cd /tmp && curl --location "${URL}" | tar xz \
	&& cd "cphalcon-${VERSION}/build" && ./install && cd - \
	&& rm -rf "/tmp/cphalcon-${VERSION}/" \
	&& echo \
		"extension=phalcon" \
		> /usr/local/etc/php/conf.d/phalcon.ini
