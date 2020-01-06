FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8

RUN \
    apt-get update && \
    apt-get install -y --no-install-recommends software-properties-common && \
    add-apt-repository -y ppa:ondrej/php && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    php7.1-cli php7.1-fpm php7.1-curl php7.1-bcmath php7.1-gd php7.1-geoip php7.1-gmp php7.1-imagick php7.1-intl \
    php7.1-json php7.1-mbstring php7.1-memcached php7.1-mcrypt php7.1-mysql php7.1-redis php7.1-opcache php7.1-mongodb \
    php-pear php7.1-pspell php7.1-soap php7.1-xml php7.1-zip \
    git rsync wget patch tar bzip2 unzip curl mysql-client libxext6 libxrender1 iputils-ping && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    rm -rf /var/lib/apt/lists/* /etc/php/5* /etc/php/7.0

CMD ["cat"]
