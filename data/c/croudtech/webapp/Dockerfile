FROM php:7.1-fpm

COPY ./config/apt /etc/apt/sources.list.d
RUN apt-key adv --keyserver keyserver.debian.com --recv-keys $key

# Install Packages - Please add extra packages in alphabetical order for clarity.
RUN set -x \
 && apt-key update \
 && apt-get update \
 && apt-get install -y --force-yes \
                        bash \
                        build-essential \
                        cron \
                        curl \
                        gettext \
                        git \
                        imagemagick \
                        libcurl4-openssl-dev \
                        libedit-dev \
                        libfreetype6-dev \
                        libicu-dev \
                        libjpeg62-turbo-dev \
                        libmagickcore-dev \
                        libmagickwand-dev \
                        libmcrypt-dev \
                        libmemcached-dev \
                        libmemcached11 \
                        libpcre3-dev \
                        libpng12-dev \
                        libssl-dev \
                        libxml2-dev \
                        libz-dev \
                        mysql-client \
                        nano \
                        nginx \
                        pkg-config \
                        pwgen \
                        sudo \
                        supervisor \
                        tar \
                        vim \
                        wget \
                        zip \
  && apt-get clean

# Configure PHP Extensions - Please add extra extensions in alphabetical order for clarity.
RUN docker-php-source extract \
    && git clone https://github.com/php-memcached-dev/php-memcached /usr/src/php/ext/memcached \
    && cd /usr/src/php/ext/memcached && git checkout -b php7 origin/php7 \
    && docker-php-ext-configure memcached --with-libmemcached-dir \
    && docker-php-ext-install   calendar \
                                iconv \
                                intl \
                                mcrypt \
                                memcached \
                                mysqli \
                                opcache \
                                pcntl \
                                pdo \
                                pdo_mysql \
                                soap \
                                zip \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && pecl install mongodb \
    && pecl install imagick \
    && docker-php-ext-enable mongodb \
    && docker-php-source delete \
    && docker-php-ext-enable imagick

# Configure PHP
COPY config/php/* /usr/local/etc/php/
COPY config/php-fpm/php-fpm.d/* /usr/local/etc/php-fpm.d/
RUN mkdir -p /var/log/php-fpm && chown www-data:www-data /var/log/php-fpm

# Install Composer Package Manager
USER root
COPY install_composer.sh /usr/bin/install_composer.sh
RUN /usr/bin/install_composer.sh

# Set up NGINX
USER www-data
COPY config/nginx/nginx.conf /etc/nginx/nginx.conf.template
COPY config/nginx/sites-available/app.conf.template /etc/nginx/sites-available/app.conf.template
COPY webapp /var/www/webapp

# Configure Supervisor
USER root
RUN mkdir -p /var/log/supervisor \
    && mkdir -p /etc/supervisor.d
COPY config/supervisor/supervisord.conf.template /etc/supervisord.conf.template
COPY config/supervisor/supervisor.d/supervisord.ini.template /etc/supervisor.d/supervisord.ini.template
COPY config/supervisor/supervisor.d/php-fpm.ini /etc/supervisor.d/php-fpm.ini
COPY config/supervisor/supervisor.d/nginx.ini /etc/supervisor.d/nginx.ini
COPY config/supervisor/supervisor.d/cron.ini /etc/supervisor.d/cron.ini

# Copy Scripts
RUN mkdir -p /etc/container_start_scripts
COPY scripts/container_start_scripts/* /etc/container_start_scripts/
COPY scripts/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
COPY scripts/run-on-leader-wrapper.sh /usr/local/bin/run-on-leader-wrapper.sh
RUN chmod -R +x /etc/container_start_scripts/*

# Install stack support scripts
RUN wget https://github.com/rancher/giddyup/releases/download/v0.16.0/giddyup && \
  mv giddyup /usr/bin/giddyup && \
  chmod +x /usr/bin/giddyup

# Set up arguments
ARG USE_DEFAULT_VHOST
ARG CONFIG_DIR
ARG SUPERVISOR_USER
ARG SUPERVISOR_PASS
ARG DOC_ROOT
ARG PHP_FPM_HOST
ARG NGINX_HOST

# Set up environment variables
ENV USE_DEFAULT_VHOST 1
ENV CONFIG_DIR /etc/supervisor_config
ENV SUPERVISOR_USER supervisoradmin
ENV DOC_ROOT /var/www/webapp
ENV WEBAPP_ROOT $DOC_ROOT
ENV PHP_FPM_HOST 127.0.0.1
ENV NGINX_HOST localhost
ENV APP_ENV $APP_ENV
ENV EXTRA_CONTAINER_START_SCRIPTS $WEBAPP_ROOT/container_startup_scripts

# Used for environment substitution in config files
ENV DOLLAR=$

VOLUME ["/etc/supervisor/supervisor.d", "/etc/nginx/conf.d", "/etc/nginx/sites-enabled", "/var/www/webapp"]

EXPOSE 80
EXPOSE 443
EXPOSE 9000

USER root
RUN chown -R www-data:www-data /var/www
WORKDIR /var/www/webapp

ENTRYPOINT ["docker-entrypoint.sh"]
CMD /usr/bin/supervisord --pidfile /var/run/supervisord.pid --nodaemon --configuration /etc/supervisor/supervisord.conf
