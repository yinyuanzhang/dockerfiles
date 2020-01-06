FROM php:7.0-apache

ENV CHEKY_VERSION=3.8.1

VOLUME ["/data"]

RUN apt-get update && \
    apt-get install -y unzip cron supervisor && \
    docker-php-ext-install mysqli && \
    cd /var/www/html && \
    curl -L -o source.zip https://github.com/Blount/Cheky/archive/${CHEKY_VERSION}.zip && \
    unzip source.zip && \
    mv Cheky-${CHEKY_VERSION}/* . && \
    chown -R www-data:www-data /var/www/html && \
    apt-get remove -y unzip && \
    rm -rf /var/lib/apt/lists/* Cheky-${CHEKY_VERSION} source.zip var && \
    ln -s /data /var/www/html/var

COPY ./entrypoint.sh /entrypoint.sh
COPY ./supervisor.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./cheky-update.cron /etc/crontab

ENTRYPOINT ["/entrypoint.sh"]
