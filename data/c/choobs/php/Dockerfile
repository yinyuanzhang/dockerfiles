FROM alpine:latest
MAINTAINER Erik DeLamarter <erik.delamarter@choobs.com>

RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk add --update \
		git \
		php7@testing \
		php7-ctype@testing \
		php7-json@testing \
		php7-openssl@testing \
		php7-phar@testing \
		php7-xml@testing \
		&& rm -rf /var/cache/apk/*

RUN ln -s /usr/bin/php7 /usr/bin/php && ln -s /etc/php7 /etc/php

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

CMD ["php", "-a"]