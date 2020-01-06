FROM drupal:7
MAINTAINER Justin Burns <justin.burns@watech.wa.gov>

ENTRYPOINT ["/entrypoint.sh"]

# create private files folder (I guess...)
RUN mkdir /var/www/private
RUN chmod ug+rw /var/www/private

RUN apt-get -q update
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq --no-install-recommends install \
	file \
    libfreetype6 \
    libjpeg62 \
    libpng12-0 \
    libpq-dev \
    libx11-6 \
    libxpm4 \
    mysql-client \
    postgresql-client \
 && BUILD_DEPS="libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng12-dev libxpm-dev re2c zlib1g-dev"; \
    DEBIAN_FRONTEND=noninteractive apt-get -yq --no-install-recommends install $BUILD_DEPS \
 && docker-php-ext-configure gd \
        --with-jpeg-dir=/usr/lib/x86_64-linux-gnu --with-png-dir=/usr/lib/x86_64-linux-gnu \
        --with-xpm-dir=/usr/lib/x86_64-linux-gnu --with-freetype-dir=/usr/lib/x86_64-linux-gnu \
 && docker-php-ext-install gd mbstring pdo_mysql pdo_pgsql zip \
 && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false $BUILD_DEPS \
 && rm -rf /var/lib/apt/lists/* \
 && pecl install uploadprogress

# Install Composer.
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

# Install Drush 7.
RUN composer global require drush/drush:8.*
RUN composer global update

# Unfortunately, adding the composer vendor dir to the PATH doesn't seem to work. So:
RUN ln -s /root/.composer/vendor/bin/drush /usr/local/bin/drush

# Add PHP-settings
ADD php-conf.d/ $PHP_INI_DIR/conf.d/

# Copy core files, fix perms on shell script
ADD entrypoint.sh README.md  /
RUN chmod uga+x /entrypoint.sh

# Copy scripts (run during launch) and sites (contains the settings.php file)
ADD /scripts/ /scripts/
ADD /sites/ sites/

VOLUME /var/www/html/sites/all/
VOLUME /var/www/html/sites/default/files/

EXPOSE 80 443
