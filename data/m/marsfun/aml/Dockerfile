FROM ubuntu:16.04

RUN apt-get -y update \
	&& apt-get install -y --no-install-recommends fortune cowsay \
	&& rm -rf /var/lib/apt/lists/*
CMD  /usr/games/fortune |/usr/games/cowsay
