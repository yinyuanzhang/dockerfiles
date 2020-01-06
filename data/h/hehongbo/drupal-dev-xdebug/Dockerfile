FROM drupal:8.8.1-apache

WORKDIR /var/www/html
RUN chown -R www-data:www-data .

RUN pecl install xdebug && \
	docker-php-ext-enable xdebug

RUN apt-get update && \
    apt-get install -y --no-install-recommends git unzip sudo && \
    rm -rf /var/lib/apt/lists/*

RUN curl https://getcomposer.org/installer | php -- --install-dir /usr/bin --filename composer && \
	mv /root/.composer /var/www/ && \
	chown -R www-data:www-data /var/www/.composer

RUN sudo COMPOSER_MEMORY_LIMIT=-1 -u www-data composer --no-cache require --dev drupal/twig_xdebug
RUN sudo COMPOSER_MEMORY_LIMIT=-1 -u www-data composer --no-cache require drush/drush

ENV XDEBUG_REMOTE_HOST 127.0.0.1
ENV XDEBUG_REMOTE_PORT 9000

RUN { \
		echo 'xdebug.remote_enable=1'; \
		echo 'xdebug.remote_host=${XDEBUG_REMOTE_HOST}'; \
		echo 'xdebug.remote_port=${XDEBUG_REMOTE_PORT}'; \
	} >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini