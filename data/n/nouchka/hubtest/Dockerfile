ARG  BASE_IMAGE=stable
FROM debian:${BASE_IMAGE}
LABEL maintainer="Jean-Avit Promis docker@katagena.com"

ARG PHPVERSION=5
ARG PHPCONF=/etc/php/5

RUN echo "$PHPVERSION $PHPCONF" && \
	cat /etc/debian_version && \
	[ "$PHPVERSION" != "5" ] || echo "specific for version 5" && \
	echo "global setup"
