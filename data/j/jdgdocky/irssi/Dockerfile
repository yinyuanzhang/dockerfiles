FROM debian:stretch-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
	ca-certificates \
	build-essential \
	libglib2.0-dev \
	libssl-dev \
	libdatetime-perl \
	libncurses-dev \
	screen \
	libwww-perl \
	pkg-config \
	automake \
	dh-autoreconf \
	cmake \
	git \
	&& rm -rf /var/lib/apt/lists/*

ENV HOME /home/user
RUN useradd --create-home --home-dir $HOME user \
	&& mkdir -p $HOME/.irssi \
	&& chown -R user:user $HOME

ENV LANG C.UTF-8
ENV IRSSI_VERSION 1.2.0
ENV FISH_VERSION 1.6

RUN git clone https://github.com/irssi/irssi \
	&& cd /irssi \
	&& git checkout tags/$IRSSI_VERSION \
	&& ./autogen.sh \
	&& make \
	&& make install

RUN git clone https://github.com/falsovsky/FiSH-irssi.git \
	&& cd /FiSH-irssi \
	&& git checkout tags/$FISH_VERSION \
	&& cmake . \
	&& make \
	&& make install
	
RUN git clone https://github.com/juliandegroot/irssi-blowfish-docker.git \
	&& chmod +x /irssi-blowfish-docker/irssi_startup.sh

WORKDIR /irssi-blowfish-docker

#After logging in to console execute after chmod+x these files: ./screencmd1.sh && ./screencmd2.sh
