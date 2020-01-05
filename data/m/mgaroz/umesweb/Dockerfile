FROM wordpress:5-fpm
RUN pecl install redis
RUN apt update && apt install wget libfcgi-bin -y
RUN bash -c "echo extension=redis.so > /usr/local/etc/php/conf.d/redis.ini" && wget -O /usr/local/bin/php-fpm-healthcheck \
https://raw.githubusercontent.com/renatomefi/php-fpm-healthcheck/master/php-fpm-healthcheck \
&& chmod +x /usr/local/bin/php-fpm-healthcheck
RUN set -xe && echo "pm.status_path = /status" >> /usr/local/etc/php-fpm.d/zz-docker.conf
