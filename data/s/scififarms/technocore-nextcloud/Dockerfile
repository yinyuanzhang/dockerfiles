FROM nextcloud:17

# I found most of this list at: https://www.reddit.com/r/NextCloud/comments/a1ftq1/nextcloud_docker_image_with_cronjob/
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    expect \
    default-mysql-client \
    libmagickwand-dev \
    libmagickcore-6.q16hdri-3-extra \
    ffmpeg && \
    pecl config-set php_ini /usr/local/etc/php && \
    docker-php-ext-enable imagick && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

ENV NEXTCLOUD_UPDATE=1

## Set up the CMD as well as the pre and post hooks.
COPY go-init /bin/go-init
COPY nextcloud/entrypoint.sh /usr/bin/entrypoint.sh
COPY exitpoint.sh /usr/bin/exitpoint.sh

RUN mkdir /nextcloud-data; \
    chown -R www-data:www-data /nextcloud-data*

VOLUME /nextcloud-data/

# The hope is that this will allow 
COPY config.php /etc/nextcloud/technocore.config.php
RUN ln -s  /etc/nextcloud/technocore.config.php /usr/src/nextcloud/config/technocore.config.php 

ENTRYPOINT ["go-init"]

COPY dogfish/ /usr/share/dogfish
COPY shell-migrations/ /usr/share/dogfish/shell-migrations
RUN ln -s /usr/share/dogfish/dogfish /usr/bin/dogfish
RUN mkdir /var/lib/dogfish 
# Need to do this all together because ultimately, the config folder is a volume, and anything done in there will be lost. 
RUN mkdir -p /var/www/html/config/ && touch /var/www/html/config/migrations.log && ln -s /var/www/html/config/migrations.log /var/lib/dogfish/migrations.log 

CMD ["-main", "entrypoint.sh /entrypoint.sh apache2-foreground", "-post", "/usr/bin/exitpoint.sh"]
