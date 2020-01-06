# PHPUnit 5.7.19 Docker Container.
FROM ubuntu:xenial

# Author
MAINTAINER Roy Evangelista <royevangelista@gmail.com>

# Update and install software properties
RUN apt-get update && \
    apt-get install -y software-properties-common python-software-properties

# Install git, curl, wget and memcache header files
RUN apt-get install -y git curl wget libmemcached-dev

# Install required PHP packages
RUN apt-get install -y --force-yes php php-common php-mcrypt php-mysql php-curl \
    php-cli php-gd php-intl php-mbstring php-json php-opcache \
    php-xsl php-zip php-xml php-memcached

# Clean
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download and install phpunit 5.7.19
RUN wget https://phar.phpunit.de/phpunit-5.7.19.phar && \
    chmod +x phpunit-5.7.19.phar && \
    mv phpunit-5.7.19.phar /usr/local/bin/phpunit

# Download and install composer
RUN curl -sS https://getcomposer.org/installer | \
    php -- --install-dir=/usr/local/bin --filename=composer

CMD ["phpunit"]
