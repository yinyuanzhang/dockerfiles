FROM debian:stable

RUN apt-get update \
	&& apt-get -y install calibre \
	&& rm -Rf /var/lib/apt/lists/*

ENTRYPOINT /usr/bin/ebook-convert
