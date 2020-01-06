FROM eloygc/docker-php:latest

ARG USER=root
ARG PASSWORD=root

ARG COMPOSER_VERSION=1.3.2
ARG XDEBUG_VERSION=2.5.1

RUN apk add --no-cache \
        php7-dev \
        php7-dom \
        php7-xdebug \
        php7-pdo_sqlite \
        php7-pear \
        openssh \
        supervisor \
        autoconf \
        git \
        curl \
        wget \
        apache-ant \
        zip \

    && rm -rf /var/cache/apk/* \

    && sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \
    && echo "${USER}:${PASSWORD}" | chpasswd \
    && ssh-keygen -A \

    && cd \
    && rm -rf /tmp/* \

    && curl -sS https://getcomposer.org/installer | php7 -- --install-dir=/usr/bin --filename=composer --version=${COMPOSER_VERSION} \
    && composer global require "hirak/prestissimo:0.3.6" \

    && wget https://git.io/psysh \
    && chmod +x psysh \
    && mv psysh /usr/bin/psysh

ADD config /

COPY tooling/* /usr/local/bin/


RUN HOST_IP="$(/sbin/ip route|awk '/default/ { print $3 }')" \
    && sed -i "$ a\xdebug.remote_host=${HOST_IP}" /etc/php7/conf.d/xdebug.ini

CMD ["supervisord", "--nodaemon", "--configuration", "/etc/supervisor/conf.d/supervisord.conf"]

EXPOSE 22 9000