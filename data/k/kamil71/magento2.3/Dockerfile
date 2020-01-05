#
# Magento2.3 Docker Image
#
# Project: https://github.com/LaFamilia-jo/shop
#
# Maintainer:
#   - Kamil Pathan <kamil.pathan@krishtechnolabs.com>

# Use 'php:7.2-fpm' as a base image.
FROM php:7.2-fpm
# Set the SHELL option '-o pipefail'
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install required Magento packages using package manager
RUN apt-get update && apt-get install -y --no-install-recommends curl gnupg2 \
&& apt-get install -y --no-install-recommends \
      cron \
      gzip \
      libfreetype6-dev \
      libicu-dev \
      libjpeg62-turbo-dev \
      libmcrypt-dev \
      libpng-dev \
      libxslt1-dev \
      lsof \
      mysql-client \
      zip \
&& rm -rf /var/lib/apt/lists/* \
# Configure the gd library
&& docker-php-ext-configure \
    gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
# Install required PHP extensions
&& docker-php-ext-install \
      gd \
      intl \
      pdo_mysql \
      xsl \
      zip \
      soap \
      bcmath \
# Install Xdebug (but don't enable)
&& pecl install -o -f xdebug \
# Install and configure Composer. Add execute permissions and move to /usr/bin
&& curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/bin/composer && chmod +x /usr/bin/composer \
# Create path for FPM socket
&& mkdir -p /var/run/php \
# Assign shell for 'www-data'
&& usermod -s /bin/bash www-data

# Define environment variables.
ENV PROJECT_NAME="magento-test" \
    MAGENTO_HOME="/home/www-data/magento" \
    MAGENTO_ROOT="/var/www/magento" \
    WEB_ROOT="/var/www/magento" \
    COMPOSER_TMP="/tmp/composer" \
    COMPOSER_ROOT="/home/www-data/composer" \
    WORKSPACE="/dockerfiles" \
    PHP_FPM_CONFIG="/usr/local/etc/php"


# Install all dependencies defined in 'composer.json'
WORKDIR $COMPOSER_TMP
COPY magento/app/etc/vendor_path.php ./app/etc/vendor_path.php
COPY magento/composer.json .
COPY magento/auth.json .
RUN composer install \
    && chown -R www-data: $COMPOSER_TMP/vendor

# Copy PHP FPM configuration
ADD conf/php-fpm.ini /usr/local/etc/php/conf.d/zz-magento.ini
ADD conf/php-fpm.conf /usr/local/etc/php-fpm.d/

# Change working direcoty to $MAGENTO_HOME
WORKDIR $MAGENTO_HOME

# Copy all Magento files to $MAGENTO_HOME
COPY --chown=www-data magento/ .

RUN rm -rf /home/www-data/magento/vendor 

WORKDIR $MAGENTO_HOME
# Applying magento permissions
RUN find var generated pub/static pub/media app/etc -type f -exec chmod g+w {} + && find var generated pub/static pub/media app/etc -type d -exec chmod g+ws {} + \
 && chown -R www-data:www-data *

# Copy 'entrypoint.sh'
COPY entrypoint.sh $WORKSPACE/scripts/entrypoint.sh

# Copy php.ini
COPY conf/php.ini $PHP_FPM_CONFIG/php.ini

# Execute permission changes
RUN chmod -R +x $WORKSPACE/scripts/ \
 && chmod -R u+x bin/magento 

# Expose FPM port
EXPOSE 9000 80

# Run entrypoint script
ENTRYPOINT [ "/dockerfiles/scripts/entrypoint.sh" ]

# Define command to run after the entrypoint exists
CMD ["php-fpm","--nodaemonize", "--fpm-config=/usr/local/etc/php-fpm.d/php-fpm.conf"]
