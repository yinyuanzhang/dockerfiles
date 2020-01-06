FROM composer:1.6

RUN apk add rsync npm libpng-dev icu-dev g++ libxml2-dev libxslt-dev file autoconf nasm libtool automake jq tree && \
    docker-php-ext-install gd bcmath intl soap xsl pdo_mysql && \
    /usr/bin/npm install grunt -g 
