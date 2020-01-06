FROM jawira/base

MAINTAINER Jawira Portugal

#https://serverfault.com/questions/683605/docker-container-time-timezone-will-not-reflect-changes
ENV TZ=Europe/Brussels
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
    php7.2 \
    php7.2-cli \
    php7.2-curl \
    php7.2-mbstring \
    php7.2-xml \
    php7.2-zip \
    && apt-get autoremove -y \
    && apt-get autoclean \
    && apt-get clean \
    && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

#    php7.2-common \
#    php7.2-curl \
#    php7.2-dev \
#    php7.2-json \
#    php7.2-ldap \
#    php7.2-mysql \
#    php7.2-opcache \
#    php7.2-readline \
#    php7.2-tidy \
#    php7.2-xmlrpc \
#    php7.2-bz2 \
#    php7.2-fpm \
#    php7.2-imap \
#    php7.2-intl \
#    php7.2-soap \
#    php7.2-xsl
