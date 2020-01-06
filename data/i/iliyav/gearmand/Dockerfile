FROM ubuntu:trusty

RUN \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
        apt-get -y install \
            curl \
            gearman-job-server \
            gearman-tools \
            git \
            php5-cli \
            supervisor
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer

RUN \
    git clone git://github.com/gaspaio/gearmanui.git /gearman-ui && \
    cd /gearman-ui && \
    composer install && \
    cp app/config/gearmanui.yml.dist app/config/gearmanui.yml

COPY index.php /gearman-ui/web/index.php
COPY supervisor.conf /etc/supervisor/conf.d/supervisor.conf

EXPOSE 4730 4731

CMD ["/usr/bin/supervisord"]