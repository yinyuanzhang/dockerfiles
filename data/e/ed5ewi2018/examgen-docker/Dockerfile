FROM phpdockerio/php72-fpm:latest
WORKDIR "/application"

# Fix debconf warnings upon build
ARG DEBIAN_FRONTEND=noninteractive

# Install selected extensions and other stuff
RUN apt-get update \
    && apt-get -y install php7.2-mysql php-xdebug php-pear libmcrypt-dev libreadline-dev php7.2-dev git texlive-full \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

RUN echo "openin_any = p" >> /etc/texmf/texmf.d/examGenerator.cnf
RUN update-texmf