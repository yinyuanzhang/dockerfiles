FROM debian:stretch

LABEL mantainer="ocutrin@gmail.com"

ENV GOSU_VERSION 1.10
ENV ARCHITECTURE amd64
ENV IDIOMA es_ES
ENV DEBIAN_FRONTEND noninteractive

RUN set -ex \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends $PACKAGES ca-certificates wget gnupg2 dirmngr locales nano gosu

RUN localedef -i $IDIOMA -c -f UTF-8 -A /usr/share/locale/locale.alias $IDIOMA.UTF-8 \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gosu nobody true

ENV LANG $IDIOMA.utf8

RUN apt-get purge -y --auto-remove ca-certificates wget gnupg2 dirmngr \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* $GNUPGHOME /usr/local/bin/gosu.asc
