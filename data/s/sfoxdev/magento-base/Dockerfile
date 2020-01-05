FROM ubuntu:16.04
MAINTAINER SFoxDev <admin@sfoxdev.com>

ENV DEBIAN_FRONTEND="noninteractive" \
    LC_ALL="C.UTF-8" \
    LANG="en_US.UTF-8" \
    LANGUAGE="en_US.UTF-8" \
    MAGENTO_VERSION="2.1.9" \
    INSTALL_PKG="mc inetutils-ping php-xdebug" \
    SERVER_NAME="sfoxdev.com" \
    MAGENTO_ADMINURL="admin" \
    MYSQL_HOST="sfoxdev.com" \
    MYSQL_USER="magento2" \
    MYSQL_PASSWORD="magento2" \
    MYSQL_DATABASE="magento3" \
    MAGENTO_URL="http://sfoxdev.com" \
    MAGENTO_SECUREURL="https://sfoxdev.com" \
    MAGENTO_LOCALE="en_US" \
    MAGENTO_TIMEZONE="Europe/Kiev" \
    MAGENTO_DEFAULT_CURRENCY="UAH" \
    MAGENTO_ADMIN_FIRSTNAME="MyStore" \
    MAGENTO_ADMIN_LASTNAME="Admin" \
    MAGENTO_ADMIN_EMAIL="admin@sfoxdev.com" \
    MAGENTO_ADMIN_USERNAME="admin" \
    MAGENTO_ADMIN_PASSWORD="1q2w3e4r" \
    MAGENTO_USE_REWRITES="0" \
    MAGENTO_SECURE="0" \
    MAGENTO_SECUREADMIN="0"

RUN set -ex ; \
    apt-get -y update && apt-get -y upgrade ; \
    apt-get -y install \
      apache2 libapache2-mod-php7.0 cron mysql-client curl \
      php7.0 php7.0-mysql php7.0-dom php7.0-simplexml php7.0-curl php7.0-intl php7.0-xsl php7.0-mbstring php7.0-zip php7.0-xml \
      php7.0-bcmath php7.0-gd php7.0-mcrypt php7.0-soap php7.0-json php7.0-iconv php-imagick \
      ${INSTALL_PKG} ; \
    a2enmod rewrite ;

ADD conf/ /

RUN cd /var/www/html ; \
    rm /var/www/html/index.html ; \
    sed -i "s/SERVER_NAME/${SERVER_NAME}/g" /etc/apache2/apache2.conf ; \
    echo "===== Drop database if exist =====" ; \
    mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD} -h${MYSQL_HOST} -v -e "DROP DATABASE IF EXISTS ${MYSQL_DATABASE}" ; \
    echo "===== Create database =====" ; \
    mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD} -h${MYSQL_HOST} -v -e "CREATE DATABASE ${MYSQL_DATABASE}" ; \
    echo "============== Install composer package ==============" ; \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer ; \
    echo "============== Installing Magento with Composer ==============" ; \
    php /usr/local/bin/composer create-project --prefer-dist \
        --repository-url=https://repo.magento.com/ magento/project-community-edition=${MAGENTO_VERSION} /var/www/html ; \
    echo "============== Chmod files ==============" ; \
    cd /var/www/html ; \
    find . -type d -exec chmod 700 {} \; && find . -type f -exec chmod 600 {} \; ;

RUN cd /var/www/html ; \
    echo "============== php bin/magento setup:install ==============" ; \
    php bin/magento setup:install \
      --use-sample-data \
      --base-url="${MAGENTO_URL}" \
      --base-url-secure="${MAGENTO_SECUREURL}" \
      --db-host="${MYSQL_HOST}" \
      --db-name="${MYSQL_DATABASE}" \
      --db-user="${MYSQL_USER}" \
      --db-password="${MYSQL_PASSWORD}" \
      --admin-firstname="${MAGENTO_ADMIN_FIRSTNAME}" \
      --admin-lastname="${MAGENTO_ADMIN_LASTNAME}" \
      --admin-email="${MAGENTO_ADMIN_EMAIL}" \
      --admin-user="${MAGENTO_ADMIN_USERNAME}" \
      --admin-password="${MAGENTO_ADMIN_PASSWORD}" \
      --language="${MAGENTO_LOCALE}" \
      --currency="${MAGENTO_DEFAULT_CURRENCY}" \
      --timezone="${MAGENTO_TIMEZONE}" \
      --use-rewrites="${MAGENTO_USE_REWRITES}" \
      --use-secure="${MAGENTO_SECURE}" \
      --use-secure-admin="${MAGENTO_SECUREADMIN}" \
      --backend-frontname="${MAGENTO_ADMINURL}" ; \
    echo "============== Chmod files ==============" ; \
    chmod -R 755 /var/www/html/ ; \
    chmod -R 777 /var/www/html/app/etc ; \
    chmod -R 777 /var/www/html/var/ ; \
    chmod -R 777 /var/www/html/pub/ ; \
    chmod 755 /var/www/html/bin/magento ; \
    chown -R www-data:www-data /var/www/html/ ; \
    echo "============== Make dump files and database ==============" ; \
    mkdir /root/magento-data ; \
    cd /root/magento-data ; \
    tar -czf magento-html.tar.gz -P /var/www/html ; \
    mysqldump -u${MYSQL_USER} -p${MYSQL_PASSWORD} -h${MYSQL_HOST} ${MYSQL_DATABASE} > /root/magento-data/magento-database.sql ; \
#    gzip < magento-database.sql > magento-database.sql.gz ; \
    echo "============== Secure environment ==============" ; \
    unset INSTALL_PKG ; \
    unset SERVER_NAME ; \
    unset MAGENTO_ADMINURL ; \
    unset MYSQL_HOST ; \
    unset MYSQL_USER ; \
    unset MYSQL_PASSWORD ; \
    unset MYSQL_DATABASE ; \
    unset MAGENTO_URL ; \
    unset MAGENTO_SECUREURL ; \
    unset MAGENTO_LOCALE ; \
    unset MAGENTO_DEFAULT_CURRENCY ; \
    unset MAGENTO_TIMEZONE ; \
    unset MAGENTO_USE_REWRITES ; \
    unset MAGENTO_SECURE ; \
    unset MAGENTO_SECUREADMIN ; \
    unset MAGENTO_ADMIN_FIRSTNAME ; \
    unset MAGENTO_ADMIN_LASTNAME ; \
    unset MAGENTO_ADMIN_EMAIL ; \
    unset MAGENTO_ADMIN_USERNAME ; \
    unset MAGENTO_ADMIN_PASSWORD ; \

    apt-get clean autoclean ; \
    apt-get autoremove --yes ; \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ; \
    echo "============== Installation finished ==============" ;

EXPOSE 80

VOLUME ["/var/www/html"]

CMD ["apachectl", "-D", "FOREGROUND"]
