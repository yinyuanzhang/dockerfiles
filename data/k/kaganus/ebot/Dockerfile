FROM php:5.6.25-zts

ENV EBOT_HOME="/ebot" \
    TIMEZONE="Europe/Istanbul"

RUN apt-get update -y && curl -sL https://deb.nodesource.com/setup_8.x | bash && \
    apt-get install -y netcat git nodejs php5-curl && apt-get clean && \
    mkdir ${EBOT_HOME} && \
    npm install socket.io archiver formidable && \
    npm install -g forever && \
    pecl install pthreads-2.0.10 && \
    docker-php-ext-enable pthreads && \
    docker-php-ext-install mysql sockets && \
    echo 'date.timezone = "${TIMEZONE}"' >> /usr/local/etc/php/conf.d/php.ini && \
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php --install-dir=/usr/bin && \
    php -r "unlink('composer-setup.php');" && \
    git clone https://github.com/kaganus/eBot-CSGO.git "$EBOT_HOME" && \
    cd "$EBOT_HOME" && git checkout "master" && \
    /usr/local/bin/php /usr/bin/composer.phar install && \
    cp "$EBOT_HOME"/config/config.ini.smp "$EBOT_HOME"/config/config.ini

WORKDIR ${EBOT_HOME}

COPY entrypoint.sh /sbin/entrypoint.sh

RUN chmod +x /sbin/entrypoint.sh

EXPOSE 12360 12360/udp 12361/udp

ENTRYPOINT ["/sbin/entrypoint.sh"]
