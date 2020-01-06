FROM ubuntu:16.04
LABEL maintainer="janusz.ulanowski@heanet.ie"
ENV LANGUAGE=en_GB.UTF-8
ENV LC_ALL=en_GB.UTF-8
ENV LANG=en_GB.UTF-8
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

ARG DEBIAN_FRONTEND=noninteractive

RUN \
	apt-get update &&\
	apt-get -y dist-upgrade &&\
        apt-get clean &&\
	mkdir -p /opt/tools/bin


RUN \
	apt-get -y install locales\
	software-properties-common\
	python-software-properties\
        openssl\
        curl \ 
	git\
	xmlsec1\
	ca-certificates\
	wget\
	unzip\
	less\
	net-tools\
	vim\
	openjdk-9-jre-headless\
	supervisor\
        python-pika\
	language-pack-en &&\
        apt-get clean 

RUN \
	add-apt-repository -y -u ppa:ondrej/php &&\
	apt-get -y install php7.1\
	php7.1-bcmath\
	php7.1-xml\
	php7.1-mbstring\
	php7.1-gmp\
	php7.1-curl\
	php7.1-mysql\
	php7.1-mcrypt &&\
	apt-get -y install php7.1-cli &&\
	apt-get -y install php-redis &&\
	apt-get -y install php-memcached &&\
	apt-get -y install php7.1-gd &&\
	apt-get -y install php7.1-imagick &&\
        cd /root &&\
        curl -O http://pkg.switch.ch/switchaai/SWITCHaai-swdistrib.asc &&\
        gpg --with-fingerprint  SWITCHaai-swdistrib.asc &&\
        apt-key add SWITCHaai-swdistrib.asc &&\
        echo 'deb http://pkg.switch.ch/switchaai/ubuntu xenial main' | tee /etc/apt/sources.list.d/SWITCHaai-swdistrib.list > /dev/null &&\
        apt-get update &&\
        apt-get -y install --install-recommends shibboleth &&\
        apt-get -y purge libsaml8 libshibsp6 libxmltooling6v5 shibboleth-schemas &&\
        apt-get clean &&\
        rm -f /root/SWITCHaai-swdistrib.asc
RUN \
	cd /opt/tools &&\
	curl -O http://shibboleth.net/downloads/tools/xmlsectool/latest/xmlsectool-2.0.0-bin.zip &&\
	unzip xmlsectool-2.0.0-bin.zip 

##############################################
