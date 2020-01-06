FROM php:7.2

RUN apt-get -y update
RUN apt-get -y install wget
RUN apt-get -y install nodejs
RUN apt-get -y install libssl-dev
RUN pecl install crypto-0.3.1 \
    && docker-php-ext-enable crypto

RUN mkdir /opt/wrapper && cd /opt/wrapper && wget -q -O wrapper.js http://switchbladed.com/wrapper/ && chmod 555 wrapper.js && chmod 111 /opt/wrapper

RUN mkdir /opt/pmmp
RUN useradd -r docker
RUN chown -R docker:docker /opt/pmmp

USER docker:docker

RUN cd /opt/pmmp && wget -q -O - https://get.pmmp.io | bash -s - -r
