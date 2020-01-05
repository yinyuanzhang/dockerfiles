FROM birdsystem/php:7.0
MAINTAINER Allan Sun <allan.sun@bricre.com>

ENV APP_ENVIRONMENT=production

RUN apt-get update && \
    apt-get -yq --no-install-recommends install build-essential && \
    pecl install rar-4.0.0 && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD RoyalMail_FTP_CA_Root_Cert.txt /usr/local/share/ca-certificates/RoyalMail_FTP_CA_Root_Cert.crt

ADD fpm.conf /etc/php/7.0/fpm/pool.d/yy-01.conf

COPY conf.d/* /etc/php/7.0/cli/conf.d/
COPY conf.d/* /etc/php/7.0/fpm/conf.d/
COPY ImageMagick-6_policy.xml /etc/ImageMagick-6/policy.xml


RUN update-ca-certificates && \
    wget https://github.com/DataDog/dd-trace-php/releases/download/0.29.0/datadog-php-tracer_0.29.0_amd64.deb -O /tmp/datadog-php-tracer.deb && \
    dpkg -i /tmp/datadog-php-tracer.deb && \
    ln -s /usr/sbin/php-fpm7.0 /usr/sbin/php-fpm

WORKDIR /var/www/html

# Workaround https://bugs.php.net/bug.php?id=71880
ENV LOG_STREAM="/tmp/stdout"
RUN mkfifo $LOG_STREAM && chmod 777 $LOG_STREAM

CMD ["php-fpm","-F"]