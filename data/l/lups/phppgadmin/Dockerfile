FROM maxexcloo/nginx-php:latest
MAINTAINER Matthew Mckenzie <matthew.mckenzie@levelup.solutions>
ENV VERSION 5.1

RUN apt-get update && \
	apt-get install -y wget && \
	apt-get clean && \
	echo -n > /var/lib/apt/extended_states && \
	rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*

WORKDIR /app
RUN wget -q -O- "https://sourceforge.net/projects/phppgadmin/files/phpPgAdmin%20%5Bstable%5D/phpPgAdmin-${VERSION}/phpPgAdmin-${VERSION}.tar.gz/download" | tar --strip-components=1 -xz && \
	rm -rf conf/config.inc.php-dist CREDITS DEVELOPERS FAQ HISTORY INSTALL TODO TRANSLATORS
WORKDIR /
ADD app /app