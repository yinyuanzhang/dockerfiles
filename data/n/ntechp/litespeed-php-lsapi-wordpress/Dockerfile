FROM ubuntu:bionic
RUN apt-get update && \
	apt-get install -y wget && \
	wget -O - http://rpms.litespeedtech.com/debian/enable_lst_debain_repo.sh | bash && \
	apt-get install -y openlitespeed lsphp73 lsphp73-apcu lsphp73-common lsphp73-opcache lsphp73-curl lsphp73-imap lsphp73-intl lsphp73-json \
		lsphp73-memcached lsphp73-mysql lsphp73-recode \
		lsphp73-redis && \
	ln -sf /usr/local/lsws/lsphp73/bin/lsphp /usr/local/lsws/fcgi-bin/lsphp && \
	apt-get clean && \
	apt-get autoclean && \
	apt-get autoremove --purge -y wget && \
	rm -rf /var/lib/apt/lists/*

VOLUME /var/www/html

CMD ["/usr/local/lsws/bin/openlitespeed","-d"]