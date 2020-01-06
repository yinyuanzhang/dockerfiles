FROM ubuntu:xenial
# Ubuntu 18.04 (bionic) does not have pdftk

# set locale: https://stackoverflow.com/questions/28405902/how-to-set-the-locale-inside-a-ubuntu-docker-container
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
		locales \
	&& apt-get clean && rm -rf /var/lib/apt/lists/*
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# install latex utilities
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
		texlive-full \
		latexmk \
	&& apt-get clean && rm -rf /var/lib/apt/lists/*

# install pdf utilities
# pdftk: splitting pdf
# ghostscript: for gs, transforming to grayscale
# poppler-utils: for pdfinfo (length of pdf) and pdffonts (font analyzer)
# python-pygments: for minted (a latex package)
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
		pdftk \
		ghostscript \
		poppler-utils \
		python-pygments \
	&& apt-get clean && rm -rf /var/lib/apt/lists/*

# install programming utilities
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
		make \
		git-all \
		vim \
		python3-pip \
	&& apt-get clean && rm -rf /var/lib/apt/lists/*

# install pip packages
RUN pip3 install \
	requests==2.22.0 \
	matplotlib==3.0 \
	numpy==1.17.2 \
	scipy==1.3.1 \
	sympy==1.4 \
	texsoup==0.2.0 \
	pygments-lexer-solidity==0.3.1

# install pplatex: https://github.com/stefanhepp/pplatex
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
		libpcre3 \
		libpcre3-dev \
		scons \
	&& apt-get clean && rm -rf /var/lib/apt/lists/* \
	&& git clone https://github.com/stefanhepp/pplatex /opt/pplatex \
	&& cd /opt/pplatex \
	&& git checkout 5cec891ad6aec0115081cdd114ae1cc4f1ed7c06 \
	&& scons \
	&& ln -s "/opt/pplatex/bin/pplatex" "/usr/local/bin/pplatex"
