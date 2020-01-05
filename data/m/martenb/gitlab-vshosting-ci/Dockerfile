FROM php:7.2

RUN apt-get -y update && \
    apt-get -y --no-install-recommends install git openssh-client rsync zip wget

RUN curl --silent --show-error https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
