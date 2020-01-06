FROM dezinger/ubuntu-14:latest

MAINTAINER dezinger@gmail.com

ENV DEBIAN_FRONTEND noninteractive
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_RUN_DIR /var/run/apache2

COPY files/ /

RUN \ 
# install
    apt-get -y update && \
    apt-get install --no-install-recommends -y \ 
    apache2 apache2-utils && \
# configure
    mkdir -p /var/lock/apache2 /var/run/apache2 /var/webdav && \
    chown www-data /var/lock/apache2 /var/run/apache2 /var/webdav && \
    a2enmod dav dav_fs && \
    a2dissite 000-default && \
# clean
    apt-get -y autoremove && apt-get -y clean && apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
 
EXPOSE 80

WORKDIR /var/webdav

VOLUME ["/var/webdav"]