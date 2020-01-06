FROM prima/php:7.2.24-4

RUN apt-get update && \
    apt-get install -y xz-utils libxext6 libfontconfig1 libxrender-dev unzip default-mysql-client rsync && \
    apt-get install -y xfonts-base xfonts-75dpi xfonts-utils libfontenc1 xfonts-encodings fontconfig && \
    curl -L -o /opt/wkhtmltox_0.12.5-1.stretch_amd64.deb https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb && \
    dpkg -i /opt/wkhtmltox_0.12.5-1.stretch_amd64.deb && \
    rm -r /var/lib/apt/lists/* && \
    # Check that everything was installed correctly
    php -v && php-fpm -v && wkhtmltopdf --version && \
    rm -rf /usr/local/etc/fpm.d/* /usr/local/etc/php-fpm.d/

COPY files/fpm.d/* /usr/local/etc/fpm.d/
COPY files/entrypoint.sh /entrypoint.sh
COPY files/prima.ini /usr/local/etc/php/conf.d/prima.ini

ENV FPM_MAX_CHILDREN=5 \
    FPM_START_SERVERS=2 \
    FPM_MIN_SPARE_SERVERS=1 \
    FPM_MAX_SPARE_SERVERS=2 \
    PHP_MAX_EXECUTION_TIME=15

CMD ["php-fpm", "--nodaemonize"]
