FROM ubuntu:16.04

RUN apt-get update && apt-get install -y software-properties-common language-pack-en-base \
    && LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/php \
    && LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/pkg-gearman \
    && apt-get update \
    && apt-get install -y  supervisor vim mariadb-client-10.0 curl git cron

RUN apt-get install -y  php5.6 php5.6-cli php5.6-curl php5.6-fpm \
       php5.6-intl php5.6-mbstring php-pear php-gearman php5.6-gd php5.6-zip \
       php5.6-mcrypt php5.6-mysql php5.6-readline php5.6-soap php5.6-tidy php-uuid php-xdebug php5.6-xsl \
       supervisor vim \
       mariadb-client-10.0 \
    && mkdir /run/php

RUN apt-get install -y python-pip python-dev

RUN pip install ansible

RUN apt-get install -y default-jdk

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN sed -i -e 's/listen = \/run\/php\/php5.6-fpm.sock/listen = 0.0.0.0:9000/g' /etc/php/5.6/fpm/pool.d/www.conf \
    && sed -i -e 's/;catch_workers_output.+$/catch_workers_output = yes/g' /etc/php/5.6/fpm/pool.d/www.conf \
    && echo "" >>  /etc/php/5.6/fpm/pool.d/www.conf \
    && echo "php_flag[display_errors] = on" >>  /etc/php/5.6/fpm/pool.d/www.conf \
    && echo "php_admin_flag[log_errors] = on" >>  /etc/php/5.6/fpm/pool.d/www.conf \
    && sed -i -e 's/;daemonize = yes/daemonize = no/g' /etc/php/5.6/fpm/php-fpm.conf \
    && sed -i -r -e 's/^memory_limit.+$/memory_limit = 256M/g' /etc/php/5.6/fpm/php.ini \
    && sed -i -r -e 's/^upload_max_filesize.+$/upload_max_filesize = 20M/g' /etc/php/5.6/fpm/php.ini \
    && sed -i -r -e 's/^post_max_size.+$/post_max_size = 30M/g' /etc/php/5.6/fpm/php.ini \
    && sed -i -r -e 's/^log_errors_max_len.+$/log_errors_max_len = 65/g' /etc/php/5.6/fpm/php.ini \
    && sed -i -r -e 's/^variables_order.+$/variables_order = "EGPCS"/g' /etc/php/5.6/fpm/php.ini \
    && sed -i -r -e 's|^;date.timezone.+$|date.timezone = "Europe/Moscow"|g' /etc/php/5.6/fpm/php.ini \
    && sed -i -r -e 's|^;error_log = php_errors.*$|error_log=/tmp/php_errors.log|g' /etc/php/5.6/fpm/php.ini

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
#RUN /usr/local/bin/composer global require fxp/composer-asset-plugin  --no-interaction

WORKDIR /var/app

COPY docker-entrypoint.sh /usr/local/bin/

RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 9000

#CMD ["/usr/bin/supervisord"]
