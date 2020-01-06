FROM 1and1internet/debian-9-apache-php-7.1:latest as magentosource
MAINTAINER developmentteamserenity@fasthosts.co.uk
ARG DEBIAN_FRONTEND=noninteractive
COPY files-stage1 /

RUN chmod +x /usr/local/bin/*.expect \
    && chmod -R 777 /.composer /vendor /var/www \
    && apt-get update \
    && apt-get install -y expect tar \
    && source /keys \
    && /usr/local/bin/magento.expect \
    && cp -R /usr/local/magento2/* /var/www/html/magento2/ \
    && cd /var/www/html \
    && tar zcf magento2.tar.gz magento2


FROM 1and1internet/debian-9-apache-php-7.1:latest
MAINTAINER developmentteamserenity@fasthosts.co.uk
ARG DEBIAN_FRONTEND=noninteractive
COPY files-stage2 /
COPY --from=magentosource /var/www/html/magento2.tar.gz /tmp

RUN chmod +x /hooks/supervisord-pre.d/10_magento \
    && chmod 777 /var/www/html \
    && rm -f /etc/supervisor/conf.d/php-fpm.conf /etc/supervisor/conf.d/nginx.conf \
    && apt-get update && apt-get install -y php7.1-redis

EXPOSE 8080
ENV DOCUMENT_ROOT=html/magento2 \
    MAGENTO_ADMIN_USER=admin \
    MAGENTO_ADMIN_PASSWORD=P@55w0rd \
    MAGENTO_BASE_URL=http://localhost:8080 \
    BACKEND_FRONTNAME=admin
