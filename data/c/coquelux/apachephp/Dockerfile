FROM ubuntu:14.04

RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv 7F0CEB10
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > /etc/apt/sources.list.d/mongodb.list

RUN apt-get update && \
    apt-get install -y apache2 libapache2-mod-php5 \
                       php5 php5-apcu php5-cli php5-curl \
                       php5-gd php5-json php5-mcrypt php5-memcached php5-imap \
                       php5-mongo php5-mysql php5-sqlite \
                       python python-pip python-dev python-yaml \
                       python-requests \
                       vim-nox curl tree git \
                       mongodb-org-shell && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install pymongo==3.0.3

RUN curl -sS https://getcomposer.org/installer | \
    php -- --install-dir=/usr/bin --filename=composer
RUN curl -sS https://phar.phpunit.de/phpunit-old.phar -o /usr/bin/phpunit && \
    chmod +x /usr/bin/phpunit

RUN php5enmod imap
RUN rm /etc/apache2/sites-enabled/000-default.conf
RUN echo "ServerName webserver" > /etc/apache2/conf-enabled/servername.conf
RUN a2enmod rewrite ssl proxy proxy_http

RUN mkdir -p /etc/sites/api/jwt/
RUN openssl genrsa -out /etc/sites/api/jwt/privkey.pem 2048
RUN openssl rsa -in /etc/sites/api/jwt/privkey.pem -pubout -out /etc/sites/api/jwt/pubkey.pem

ENV APACHE_RUN_USER    www-data
ENV APACHE_RUN_GROUP   www-data
ENV APACHE_PID_FILE    /var/run/apache2.pid
ENV APACHE_RUN_DIR     /var/run/apache2
ENV APACHE_LOCK_DIR    /var/lock/apache2
ENV APACHE_LOG_DIR     /var/log/apache2

EXPOSE 80

WORKDIR /var/www

CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
