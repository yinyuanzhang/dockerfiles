FROM ubuntu:latest
MAINTAINER Karsten Schwank <karsten.schwank@iteratec.de>

RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential \
	zip \
	unzip \
	default-jre-headless \
	texlive \
	texlive-generic-recommended \
	texlive-latex-recommended \
	texlive-fonts-recommended \
	texlive-extra-utils \
	texlive-font-utils \
	texlive-xetex \
	texlive-luatex \
	fontconfig \
	fonts-lmodern \
	fonts-font-awesome \
	&& apt-get autoclean -y \
	&& apt-get clean -y \
	&& rm -rf /var/lib/apt/lists/* 

RUN useradd --create-home --shell /bin/bash --uid 1000 texuser

VOLUME /data
WORKDIR /data

USER texuser

