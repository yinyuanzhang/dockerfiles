FROM bitnami/php-fpm:5.6.40-prod

# ---- Installing PHP Extension: memcache ----
RUN apt-get update \
  && apt-get install -y libmemcached-dev openssh-client make grep autoconf gcc libc-dev wget zlib1g-dev

RUN mkdir -p /usr/tmp && cd /usr/tmp \
	&& wget http://pecl.php.net/get/memcache-2.2.7.tgz \
	&& tar -zxvf memcache-2.2.7.tgz \
	&& cd memcache-2.2.7 \
	&& phpize && ./configure --with-php-config=/opt/bitnami/php/bin/php-config \
	&& make && make install \
	&& touch /opt/bitnami/php/etc/php.ini \
	&& echo 'extension=memcache.so' >> /opt/bitnami/php/etc/php.ini

RUN echo "" >> /opt/bitnami/php/etc/php-fpm.conf \
	&& echo 'clear_env = no' >> /opt/bitnami/php/etc/php-fpm.conf