FROM ubuntu:18.04
LABEL maintainer "Vitolo Test"
LABEL description "TestWebserver"

RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get -y clean && \
    rm -r /var/cache/apt /var/lib/apt/lists/*

RUN a2ensite default-ssl && a2enmod ssl

ENV APACHE_RUN_USER=www-data \
    APACHE_RUN_GROUP=www-data \
    APACHE_LOG_DIR=/var/log/apache2

EXPOSE 80 443

CMD ["/usr/sbin/apache2ctl","-D", "FOREGROUND"]
