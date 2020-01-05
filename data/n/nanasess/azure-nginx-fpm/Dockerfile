FROM nginx:1.15-perl
MAINTAINER Kentaro Ohkouchi

# ========
# ENV vars
# ========

# ssh
ENV SSH_PASSWD "root:Docker!"

# Composer
# Updation: https://getcomposer.org/download/
ENV COMPOSER_DOWNLOAD_URL "https://getcomposer.org/installer"
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /home/.composer

#nginx
ENV NGINX_LOG_DIR "/home/LogFiles/nginx"
#php
ENV PHP_HOME "/etc/php/7.2"
ENV PHP_CONF_DIR $PHP_HOME"/cli"
ENV PHP_CONF_FILE $PHP_CONF_DIR"/php.ini"

#Web Site Home
ENV HOME_SITE "/home/site/wwwroot"

ENV DOCKER_BUILD_HOME "/dockerbuild"

# ====================
# Download and Install
# ~. essentials
# 1. php7.0-common/php7.0-fpm/php-pear/php7.0-apcu
# 2. ssh
# 3. drush
# 4. composer
# ====================

RUN apt-get update && apt install -y gnupg2 ca-certificates apt-transport-https wget \
    && wget -q https://packages.sury.org/php/apt.gpg -O- | apt-key add -
RUN echo "deb https://packages.sury.org/php/ stretch main" | tee /etc/apt/sources.list.d/php.list

# apt-get and system utilities
RUN apt-get update && apt-get install -y \
    curl apt-utils apt-transport-https debconf-utils gcc g++ make build-essential \
    zlib1g-dev git zip unzip vim \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    php7.2-dev php7.2-cli php7.2-common php7.2-mbstring php7.2-fpm php-pear \
    php7.2-apcu php7.2-gd php7.2-xml php7.2-curl php7.2-zip php7.2-pgsql php7.2-mysql \
    && rm -rf /var/lib/apt/lists/*


RUN apt-get update && apt-get install -y --no-install-recommends openssh-server \
    && echo "$SSH_PASSWD" | chpasswd

RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/bin/composer

RUN apt-get update && apt-get install -y locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen

RUN set -ex \
	&& apt-get autoremove -y

# =========
# Configure
# =========

RUN set -ex\
    && mkdir -p /home/site/html \
    && chown -R www-data:www-data /home/site/html
# ssh
COPY sshd_config /etc/ssh/

# php
COPY php.ini /etc/php/7.2/cli/php.ini
COPY www.conf /etc/php/7.2/fpm/pool.d/www.conf

# nginx
COPY nginx.conf /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/*

# =====
# final
# =====
COPY init_container.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/init_container.sh

RUN echo "<?php phpinfo(); " > /home/site/html/index.php

EXPOSE 2222 80 1337
ENTRYPOINT ["init_container.sh"]
