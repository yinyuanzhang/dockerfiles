FROM ellkinox/docker-debian:8

ENV	DEBIAN_FRONTEND noninteractive
ENV	PHPMYADMIN_VERSION 4.8.4
ENV PHP_VERSION 7.2
# install required packges
RUN	apt-get update -qq && \
	apt-get install -y curl apache2 php${PHP_VERSION} php${PHP_VERSION}-cli php${PHP_VERSION}-mysql php${PHP_VERSION}-curl php${PHP_VERSION}-mbstring mysql-client && \
	apt-get clean autoclean && \
	apt-get autoremove --yes && \
	rm -rf /var/lib/{apt,dpkg,cache,log}/

# configure apache
RUN	rm -rf /var/www/* && \
	a2enmod rewrite && \
	a2enmod ssl && \
	a2ensite default-ssl.conf

# redirect apache logs to stderr / stdout
RUN	find /etc/apache2 -type f -exec sed -ri ' \
	s!/var/www/html!/var/www!g; \
	s!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g; \
        s!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g; \
	' '{}' ';'

RUN	sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 2G/" /etc/php/${PHP_VERSION}/apache2/php.ini && \
	sed -i "s/post_max_size = 8M/post_max_size = 8G/" /etc/php/${PHP_VERSION}/apache2/php.ini

RUN curl -SL https://files.phpmyadmin.net/phpMyAdmin/${PHPMYADMIN_VERSION}/phpMyAdmin-${PHPMYADMIN_VERSION}-all-languages.tar.gz -o phpMyAdmin-${PHPMYADMIN_VERSION}-all-languages.tar.gz && \
	tar -xzf phpMyAdmin-${PHPMYADMIN_VERSION}-all-languages.tar.gz -C /var/www --strip-components=1 && \
	rm phpMyAdmin-${PHPMYADMIN_VERSION}-all-languages.tar.gz && \
	rm -rf /var/www/setup/ /var/www/examples/ /var/www/test/ /var/www/po/ /var/www/composer.json /var/www/RELEASE-DATE-${PHPMYADMIN_VERSION} && \
    chown -R www-data:www-data /var/www; \
    find /var/www -type d -exec chmod 750 {} \; ; \
    find /var/www -type f -exec chmod 640 {} \;

COPY run.sh /run.sh

RUN chmod u+rwx /run.sh

COPY config.inc.php /var/www/config.inc.php

EXPOSE 443

ENTRYPOINT ["/run.sh"]

VOLUME ["/var/log/apache2"]
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
