FROM artyomliou/php-fpm-alpine:latest AS laravelready

LABEL maintainer="ArtyomLiou <artyomliou@gmail.com>"

# Set Timezone
ARG TZ=UTC
ENV TZ ${TZ}

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# add ./vendor/bin to non-root user's bashrc (needed for phpunit)
USER www-data

RUN echo "" >> ~/.bashrc && \
    echo 'export PATH="/var/www/vendor/bin:$PATH"' >> ~/.bashrc

# Crontab
USER root

COPY ./crontab /etc/cron.d

RUN chmod -R 644 /etc/cron.d

# Composer & install deps
COPY ./install_composer.sh /opt/install_composer.sh

RUN sed -i 's/\r//g' //opt/install_composer.sh && \
    /bin/sh /opt/install_composer.sh && \
    mv composer.phar /usr/local/bin/composer && \
    chown www-data:www-data /var/www

USER www-data

RUN composer global require hirak/prestissimo

USER root

# Set default work directory
WORKDIR /var/www
