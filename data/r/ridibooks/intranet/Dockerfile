FROM ridibooks/performance-apache-base:7.1 AS builder

# Instll Node modules
WORKDIR /build/assets
COPY assets ./
RUN npm install \
&& bower install --allow-root \
&& bower prune -p --allow-root \
&& npm run-script build

# Install Composer packages
WORKDIR /build
COPY composer.json composer.lock ./
RUN composer install --optimize-autoloader



FROM ridibooks/performance-apache-base:7.1

ENV APACHE_DOC_ROOT /var/www/html/web

# Install zip, cron and PHP modules (gd, exif)
RUN apt-get update \
&& apt-get install -y \
  zip \
  cron \
  libfreetype6-dev \
  libjpeg62-turbo-dev \
  libpng12-dev \
  libxpm-dev \
  libvpx-dev \
&& docker-php-ext-configure gd \
  --with-freetype-dir=/usr/lib/x86_64-linux-gnu/ \
  --with-jpeg-dir=/usr/lib/x86_64-linux-gnu/ \
  --with-png-dir=/usr/lib/x86_64-linux-gnu/ \
  --with-xpm-dir=/usr/lib/x86_64-linux-gnu/ \
  --with-vpx-dir=/usr/lib/x86_64-linux-gnu/ \
&& docker-php-ext-install gd exif \
&& apt-get autoclean -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN mkdir -m 755 -p var/session var/cache \
&& chown -R www-data:www-data var/session var/cache

# Set PHP custom config
COPY docker/php/* /usr/local/etc/php/conf.d/

# Set cron
COPY docker/cron.d/intranet_crontab /etc/cron.d/

# Change entrypoint
COPY docker/docker-intranet-entrypoint.sh /
ENTRYPOINT ["/docker-intranet-entrypoint.sh"]
CMD ["apache2-foreground"]

COPY --from=builder /build ./
COPY . ./
