FROM pelso/php:7.3

RUN apt-get update \
 && apt-get install -y \
    htop \
    vim \
    iputils-ping \
    net-tools \
    mariadb-client \
    sqlite3 \
    postgresql-client \
    mc \
    ranger \
    wget

COPY composer-installer.sh /home/app/composer-installer.sh
RUN /home/app/composer-installer.sh \
    && rm /home/app/composer-installer.sh

RUN wget -O /usr/local/bin/phpunit https://phar.phpunit.de/phpunit-5.phar \
    && chmod +x /usr/local/bin/phpunit

RUN curl -LO https://deployer.org/deployer.phar \
    && mv deployer.phar /usr/local/bin/dep \
    && chmod +x /usr/local/bin/dep

CMD service php7.3-fpm start \
 && service php7.3-fpm restart \
 && sleep infinity

