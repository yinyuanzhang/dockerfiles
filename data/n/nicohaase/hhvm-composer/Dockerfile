FROM debian:jessie

MAINTAINER "Nico Haase" <nico@nicohaase.de>
USER root

RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0x5a16e7281be7a449 && \ 
	echo deb http://dl.hhvm.com/debian jessie main | tee /etc/apt/sources.list.d/hhvm.list && \ 
	echo deb http://http.debian.net/debian wheezy main | tee /etc/apt/sources.list.d/wheezy.list
RUN	apt-get update && \
	apt-get install -y --no-install-recommends hhvm curl ca-certificates git ssh && \ 
	apt-get install -twheezy -y --no-install-recommends subversion
RUN	curl -sS --insecure https://getcomposer.org/installer | hhvm --php && \ 
	mv composer.phar /usr/local/bin/composer.phar

ADD php-hhvm.ini /etc/hhvm/php.ini
ADD runComposer.sh /usr/local/bin/runComposer.sh
RUN chmod +x /usr/local/bin/runComposer.sh

CMD /usr/local/bin/runComposer.sh