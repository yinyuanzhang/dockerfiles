FROM keittirat/nds-php5:5-fpm
ENV LANG en_GB.UTF-8

RUN usermod -u 1000 www-data
RUN groupmod -g 1000 www-data

WORKDIR /var/www/html
COPY www /var/www/html
COPY Readme.md /var/www/html/version.md
COPY setup/database-dev.php /var/www/html/config/database.php
COPY setup/endpoint-dev.php /var/www/html/config/endpoint.php
COPY conf/.env.txt /var/www/html/.env
RUN cd /var/www/html

RUN rm -rf /tmp/* && \
    rm -rf /var/www/html/public/gentelella && \
    rm -rf /var/www/html/public/css && \
    rm -rf /var/www/html/public/js && \
    rm -rf /var/www/html/public/fonts


VOLUME /var/www/html

CMD ["php-fpm","-F"]