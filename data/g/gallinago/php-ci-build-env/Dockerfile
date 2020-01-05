FROM maciejslawik/php-fpm-xdebug:7.4

MAINTAINER Maciej Slawik <maciekslawik@gmail.com>

USER root
RUN apt-get update
RUN apt-get install -y mariadb-server mariadb-client procps git

RUN echo "service mysql start;\nmysql -e \"CREATE USER '\$MYSQL_TEST_USER'@'%'\";\nmysql -e \"GRANT ALL PRIVILEGES ON \$MYSQL_TEST_DATABASE.* to '\$MYSQL_TEST_USER'@'%'\";\nmysql -u\$MYSQL_TEST_USER -e \"CREATE DATABASE \$MYSQL_TEST_DATABASE\"" >> /var/www/create_db.sh
RUN chmod +x /var/www/create_db.sh

RUN curl -LO https://deployer.org/releases/v6.7.0/deployer.phar
RUN mv deployer.phar /usr/local/bin/dep
RUN chmod +x /usr/local/bin/dep

ENV PATH=/root/.composer/vendor/bin:$PATH

RUN composer global require gallinago/deployer-magento2:dev-master

WORKDIR /var/www/html
