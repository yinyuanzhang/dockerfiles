FROM php:7.3-apache

LABEL name="DockerPress"
LABEL version="1.2.0"
LABEL release="2019-12-16"

# WP-cli Defaults
ENV WP_CLI_CACHE_DIR "/var/www/.wp-cli/cache/"
ENV WP_CLI_PACKAGES_DIR "/var/www/.wp-cli/packages/"
ENV ADMIN_EMAIL "webmaster@localhost"

# Utilities
ENV CRON_ACTIONSCHEDULER 1
ENV CRON_MEDIA_REGENERATE 1
ENV CRON_CLEAR_TRANSIENT 1

# Wordpress Defaults
ENV WP_POST_REVISIONS true
ENV WP_LOCALE "pt_BR"
ENV WP_DEBUG false
ENV WORDPRESS_DB_PORT 3306

# Backup Settings
ENV S3_ACCESS_KEY_ID ""
ENV S3_SECRET_ACCESS_KEY ""
ENV S3_REGION "us-east-1"

# PHP.INI Settings
ENV PHP_MEMORY_LIMIT=512M
ENV PHP_UPLOAD_MAX_FILESIZE=256M
ENV PHP_MAX_EXECUTION_TIME=300
ENV PHP_EXPOSE_PHP=Off
ENV PHP_DISPLAY_ERRORS=Off
ENV PHP_DISPLAY_STARTUP_ERRORS=Off
ENV PHP_LOG_ERRORS=On

# Install System Libraries
RUN apt-get update \
    ; \
    apt-get install -y --no-install-recommends \
    sudo \
    software-properties-common \
    build-essential \
    apache2 \
    libapache2-mod-security2 \
    modsecurity-crs \
    curl \
    tcl \
    cron \
    bzip2 \
    tidy \
    sysvbanner \
    wget \
    nano \
    htop \
    zip \
    git \
    csstidy \
    unzip \
    g++ \
    zlib1g-dev \
    libjpeg-dev \
		libmagickwand-dev \
		libpng-dev \
    libz-dev \
    libpq-dev \
    libfreetype6-dev \
    libcurl4-openssl-dev \
    libaprutil1-dev \
    libssl-dev \
    libfreetype6-dev \
    libicu-dev \
    libldap2-dev \
    libmemcached-dev \
    libxml2-dev \
    libz-dev \
		libzip-dev \
    mariadb-client \
    libmagickwand-dev \
    imagemagick \
    ghostscript \
    groff \
    python \
    python-setuptools \
    python-pip \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN pip install awscli

# Configure PHP and System Libraries
RUN	docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    ; \
	  docker-php-ext-install -j "$(nproc)" \
		  bcmath \
		  exif \
		  gd \
      pdo \
      intl \
      xml \
      pdo_mysql \
      soap \
      opcache \
      mysqli \
      opcache \
      zip \
	 ; \
   printf "\n" | printf "\n" | pecl install redis \
   ; \
   pecl install imagick-3.4.4 \
      apcu-5.1.11 \
      memcached \
   ; \
	 docker-php-ext-enable imagick \
      bcmath \
      redis \
      opcache \
      apcu \
      memcached \
	 ; \
	 apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
   ; \
	 rm -rf /var/lib/apt/lists/*

# Enable apache modules
RUN a2enmod setenvif \
      headers \
      security2 \
      deflate \
      filter \
      expires \
      rewrite \
      include \
      ext_filter

# Default Volume for Apache
VOLUME /var/www/html

# Enable Apache Configs
COPY dockerpress.conf /etc/apache2/conf-available/dockerpress.conf
RUN a2enconf dockerpress

# Installing Apache mod-pagespeed
RUN curl -o /home/mod-pagespeed-beta_current_amd64.deb https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-beta_current_amd64.deb
RUN dpkg -i /home/mod-pagespeed-*.deb
RUN apt-get -f install

COPY .htaccess /var/www/.htaccess-template
COPY wp-config-sample.php /var/www/wp-config-sample.php

# Copy commands
COPY bin/* /usr/local/bin/
RUN chmod -R +777 /usr/local/bin/

# Running container startup scripts
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Default Port for Apache
EXPOSE 80

ENTRYPOINT ["entrypoint.sh"]
CMD ["apache2-foreground"]
