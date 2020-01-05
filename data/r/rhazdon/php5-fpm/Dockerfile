FROM debian:jessie
MAINTAINER Djordje Ilic <djordje.ilic@posteo.de>

ENV DEBIAN_FRONTEND noninteractive


#######################################
# Update Debian and Install Packages
#######################################
RUN apt-get update && apt-get install -y \
  php5 \
  php5-apcu \
  php5-cli \
  php5-cgi \
  php5-common \
  php5-curl \
  php5-fpm \
  php5-gd \
  php5-imagick \
  php5-imap \
  php5-intl \
  php5-json \
  php5-mcrypt \
  php5-pecl-http \
  php5-pgsql \
  php5-sqlite \
  php5-readline \
  php5-redis


#######################################
# Tweak PHP5-FPM Config
#######################################
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=1/g" /etc/php5/fpm/php.ini && \
  sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 8M/g" /etc/php5/fpm/php.ini && \
  sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 8M/g" /etc/php5/fpm/php.ini && \
  sed -i -e "s/;daemonize\s*=\s*yes/daemonize = yes/g" /etc/php5/fpm/php-fpm.conf && \
  sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" /etc/php5/fpm/pool.d/www.conf && \
  sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g" /etc/php5/fpm/pool.d/www.conf && \
  sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g" /etc/php5/fpm/pool.d/www.conf && \
  sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g" /etc/php5/fpm/pool.d/www.conf && \
  sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g" /etc/php5/fpm/pool.d/www.conf && \
  sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g" /etc/php5/fpm/pool.d/www.conf && \
  find /etc/php5/cli/conf.d/ -name "*.ini" -exec sed -i -re 's/^(\s*)#(.*)/\1;\2/g' {} \; && \
  echo "extension=imagick.so" >> /etc/php5/fpm/php.ini

RUN usermod -u 1000 www-data


#######################################
# Clean up Image
#######################################
RUN apt-get remove --purge -y software-properties-common && \
  apt-get autoremove -y && \
  apt-get clean && \
  apt-get autoclean && \
  echo -n > /var/lib/apt/extended_states && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /usr/share/man/?? && \
  rm -rf /usr/share/man/??_* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/*


#######################################
# Start Image
#######################################
EXPOSE 9000

CMD ["php5-fpm", "-F"]
