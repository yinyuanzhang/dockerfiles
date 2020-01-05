FROM kucrut/php.nginx
LABEL Maintainer="Dzikri Aziz <kvcrvt@gmail.com>" \
      Description="Tiny Tiny RSS container with NGINX & PHP-FPM 7.2 on Alpine Linux."

# Install packages
RUN apk add --update curl mariadb-client freetype libpng libjpeg-turbo libwebp zlib && \
    apk add --no-cache --virtual .php-ext-build-deps freetype-dev freetype-dev libpng-dev libjpeg-turbo-dev libwebp-dev zlib-dev && \
    NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \
    docker-php-ext-configure gd \
      --with-gd \
      --with-png-dir=/usr/include/ \
      --with-jpeg-dir=/usr/include/ \
      --with-webp-dir=/usr/include/ \
      --with-zlib-dir \
      --with-freetype-dir=/usr/include/ && \
    docker-php-ext-configure pdo_mysql \
      --with-pdo-mysql \
      --with-zlib-dir && \
    docker-php-ext-install -j${NPROC} gd mysqli pdo_mysql pcntl && \
    apk del .php-ext-build-deps && \
    rm -fr /var/cache/apk/*

# Note that we're in /var/www/html.

# Install TT-RSS Reader.
RUN TTRSS_READER_VER=1.3.0 && \
    rm -f index.php && \
    curl -L "https://github.com/kucrut/ttrss-reader/archive/v${TTRSS_READER_VER}.tar.gz" | \
    tar -xz "ttrss-reader-${TTRSS_READER_VER}/public" --strip-components=2

# Install TT-RSS.
RUN TTRSS_VER=20180812 && \
    curl -L "https://github.com/kucrut/tt-rss/archive/${TTRSS_VER}.tar.gz" | tar -xz && \
    mv "tt-rss-${TTRSS_VER}" d

COPY config.php /var/www/html/d/

# Add Updater config to supervisord
COPY ttrss-update.conf /etc/supervisor/conf.d/

# Entrypoint to copy wp-content
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
