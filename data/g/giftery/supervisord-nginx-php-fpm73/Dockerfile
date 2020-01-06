FROM centos:7

RUN rpm -Uvh http://rpms.southbridge.ru/southbridge-rhel7-stable.rpm && \
    yum -y --nogpgcheck install epel-release southbridge-php73-release && \
    yum -y update

RUN yum -y install supervisor cronie ssmtp nginx zip p7zip jq \
    php-cli php-fpm php-opcache php-xdebug php-pdo php-mysqlnd php-mbstring php-intl php-pecl-redis php-xml php-zip php-bcmath php-soap

RUN rm -rf /var/cache/* && \
    rm -f /etc/php.d/15-xdebug.ini && \
    mkdir -p /var/cache/nginx && mkdir -p /run/php-fpm && \
    rm -f /etc/localtime && \
    ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \
    #echo "date.timezone = Europe/Moscow" > /etc/php.d/991-timezone.ini && \
    rm -rf /usr/share/doc/* /usr/share/man/* /usr/share/groff/* /usr/share/info/* /usr/share/lintian/* /usr/share/linda/*

COPY system-root/ /

WORKDIR /srv/www/php-app
EXPOSE 80
ENTRYPOINT ["/docker-entrypoint.sh"]
