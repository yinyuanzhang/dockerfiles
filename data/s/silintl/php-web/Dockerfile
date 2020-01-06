FROM silintl/apache2:latest
MAINTAINER "Phillip Shipley" <phillip_shipley@sil.org>

ENV REFRESHED_AT 2016-02-24

# Install PHP packages and enable mcrypt
RUN apt-get update -y \
	&& apt-get install -y \
        curl \
    	git \
    	php5 \
        php5-curl \
        php5-intl \
    	php5-mcrypt \
    	php5-mysql \
        s3cmd \
        rsyslog-gnutls \
	&& php5enmod mcrypt \
    && apt-get clean \
    && curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && chmod a+x /usr/local/bin/composer \
    && curl -o /usr/local/bin/whenavail https://bitbucket.org/silintl/docker-whenavail/raw/master/whenavail \
    && chmod a+x /usr/local/bin/whenavail

COPY php.ini /etc/php5/apache2/
COPY php.ini /etc/php5/cli/
COPY block_httpoxy.conf /etc/apache2/conf-enabled/
RUN chmod 0644 /etc/apache2/conf-enabled/block_httpoxy.conf \
    && chown root:root /etc/apache2/conf-enabled/block_httpoxy.conf

EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]
