FROM ibejohn818/php:php71w-base

RUN yum install -y php71w-fpm

# turn off daemon mode for docker
RUN sed -i '/daemonize /c \
daemonize = no' /etc/php-fpm.conf


RUN sed -i '/clear_env /c \
clear_env = no' /etc/php-fpm.conf

# listen for all
RUN sed -i '/^listen /c \
listen = 0.0.0.0:9000' /etc/php-fpm.d/www.conf

# allow all
RUN sed -i 's/^listen.allowed_clients/;listen.allowed_clients/' /etc/php-fpm.d/www.conf

# send php-fpm to the foregroud
ENTRYPOINT ["php-fpm"]
