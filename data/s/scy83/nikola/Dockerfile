FROM debian:jessie

MAINTAINER Tim Weber

RUN apt-get update \
	&& printf 'locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8\nlocales locales/default_environment_locale select en_US.UTF-8\n' | debconf-set-selections \
	&& apt-get install --no-install-recommends -y \
		build-essential \
		libjpeg-dev \
		libxml2-dev \
		libxslt1-dev \
		libyaml-dev \
		libzmq3-dev \
		locales \
		python3 \
		python3-dev \
		python3-pip \
		zlib1g-dev \
	&& pip3 install 'Nikola[extras]' \
	&& apt-get autoremove -y \
		build-essential \
		python3-dev \
	&& apt-get autoremove -y \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& useradd -c Nikola -m -s /bin/bash nikola

WORKDIR /home/nikola

USER nikola
