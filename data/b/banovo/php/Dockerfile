FROM banovo/php:7

ENV NODEREPO node_4.x

# Set environmental variables
ENV COMPOSER_HOME /root/composer
ENV PATH $COMPOSER_HOME/vendor/bin:$PATH
ENV LOCAL_UID 33

# Install composer
RUN set -xe \
	&& apt-get update && apt-get install -y git libfontconfig1 --no-install-recommends && rm -r /var/lib/apt/lists/* \
	&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install prestissimo for faster composer installations
RUN composer global require "hirak/prestissimo:^0.3"

# Install phpunit
RUN composer global require phpunit/phpunit 6.0.*

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

WORKDIR /var/www
EXPOSE 9000
CMD ["php-fpm"]
