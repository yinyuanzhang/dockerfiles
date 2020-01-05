FROM aesopagency/phpcli:1.1.0

MAINTAINER Aesop Agency <technical@aesopagency.com>

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /tmp

RUN apt-get update -y && \
    apt-get install -y curl git php5-curl php5-mcrypt php5-gd && \
    php5enmod mcrypt && \
    curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer && \
    composer self-update && \
    apt-get remove --purge curl -y && \
    apt-get clean

WORKDIR /data/www

ENTRYPOINT ["composer"]
CMD ["--help"]
