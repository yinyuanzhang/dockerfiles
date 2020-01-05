FROM ubuntu:18.04
LABEL maintainer="petricomp@gmail.com"

ENV WEBROOT=/var/www/html
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
	acl \
	apache2 \
	build-essential \
	fp-compiler \
	git \
	libapache2-mod-php \
	nodejs \
	octave \
	openjdk-8-jre \
	openjdk-8-jdk \
	php \
	php-cli \
	php-mbstring \
	python3 \
	python3-pip \
	pylint3 \
	sudo \
	sqlite3

RUN sed -i "s/export LANG=C/export LANG=C\.UTF-8/" /etc/apache2/envvars

RUN cd $WEBROOT && git clone https://github.com/trampgeek/jobe.git && cd $WEBROOT/jobe && /etc/init.d/apache2 start && ./install

EXPOSE 80
CMD apachectl -D FOREGROUND
