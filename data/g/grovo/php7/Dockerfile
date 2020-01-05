FROM alpine:latest
MAINTAINER Joe Violago "jviolago@grovo.com"

ENV S6_OVERLAY_VERSION=v1.17.1.1

ENV REFRESHED_AT 2017-06-05

RUN apk add --no-cache --update-cache curl ca-certificates

# Install/upgrade PHP binary and extensions.
ADD build/upgrade-php.sh /usr/bin/grovo/upgrade-php.sh
RUN chmod +x /usr/bin/grovo/upgrade-php.sh
RUN /usr/bin/grovo/upgrade-php.sh

RUN apk add --no-cache --update-cache \
        coreutils \
        nginx \
        curl \
        rsyslog && \
    curl -sSL https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz \
        | tar xz -C / && \
    sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php7/php.ini && \
    sed -i "s/;error_log = syslog/error_log = syslog/" /etc/php7/php.ini && \
    sed -i "s/expose_php = On/expose_php = Off/" /etc/php7/php.ini && \
    sed -i 's/variables_order = "GPCS"/variables_order = "EGPCS"/' /etc/php7/php.ini && \
    mkdir -p /var/www/public && \
    mkdir -p /etc/services.d/nginx && \
    mkdir -p /etc/services.d/phpfpm && \
    mkdir -p /etc/services.d/rsyslog && \
    rm -rf /etc/php7/php-fpm.d /var/www/localhost && \
    echo "/var/www true nginx 0644 0755" > /etc/fix-attrs.d/01-www-dir && \
    rm -rf /var/cache/apk/* /tmp/* /var/tmp/*

# Setup services
ADD build/php-fpm.conf /etc/php7/php-fpm.conf
ADD build/nginx.conf   /etc/nginx/nginx.conf
ADD build/nginx.sh     /etc/services.d/nginx/run
RUN chmod +x           /etc/services.d/nginx/run

ADD build/rsyslog.conf /etc/rsyslog.conf
ADD build/rsyslog.sh   /etc/services.d/rsyslog/run
RUN chmod +x           /etc/services.d/rsyslog/run

ADD build/phpfpm.sh    /etc/services.d/phpfpm/run
RUN chmod +x           /etc/services.d/phpfpm/run

EXPOSE 80

CMD ["/init"]

