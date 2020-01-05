FROM fedora:latest

LABEL maintainer.name="Luiz Fernando Pereira"
LABEL maintainer.email="luiz.fernando@outcenter.com.br"
LABEL maintainer.company="Outcenter"

RUN dnf -y install \
    php \
    php-common \
    php-cli \
    php-mbstring \
    php-xml \
    php-mysqlnd \
    php-pdo \
    php-gd \
    php-intl \
    php-interbase \
    php-zip \
    php-json \
    php-pecl-mcrypt \
    php-pecl-ssh2 \
    php-pecl-xdebug \
    php-snmp \
    nginx \
    openssl \
    openssh && \
    dnf clean all

ENV TIMEZONE=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime && echo $TIMEZONE > /etc/timezone

RUN rm /etc/php.d/15-xdebug.ini
COPY xdebug.ini /etc/php.d/15-xdebug.ini.disabled
COPY nginx.conf /etc/nginx/nginx.conf
COPY php.ini /etc/php.ini
COPY www.conf /etc/php-fpm.d/www.conf
COPY ./error-pages/*.html /usr/share/nginx/html/

COPY entrypoint.sh /usr/sbin/entrypoint.sh
RUN chmod +x /usr/sbin/entrypoint.sh \
    && mkdir /run/php-fpm && mkdir /var/www/server-test
COPY ./server-test/index.php /var/www/server-test/
RUN chown -R nginx:nginx /var/www

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl --fail http://localhost/server-test || exit 1

EXPOSE 80
EXPOSE 9000

ENTRYPOINT [ "/usr/sbin/entrypoint.sh" ]