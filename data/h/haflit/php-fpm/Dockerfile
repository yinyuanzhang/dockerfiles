FROM debian:jessie

RUN apt-get update && apt-get install -y php5-common php5-cli php5-fpm php5-mcrypt php5-mysql php5-apcu php5-gd php5-imagick php5-curl php5-intl php5-pgsql
RUN apt-get install -y php5-memcache php5-memcached

RUN rm /etc/php5/fpm/pool.d/*

ADD conf/symfony.ini /etc/php5/fpm/conf.d/
ADD conf/symfony.ini /etc/php5/cli/conf.d/

ADD conf/symfony.pool.conf /etc/php5/fpm/pool.d/

RUN usermod -u 1000 www-data

CMD ["php5-fpm", "-F"]

EXPOSE 9000