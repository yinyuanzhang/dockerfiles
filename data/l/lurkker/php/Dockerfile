FROM alpine:edge

ENV SSH_VERSION=8.1
ENV PHP_VERSION=7.3
ENV COMPOSER_VERSION=1.9
ENV XDEBUG_VERSION=2.9

RUN apk add --update --no-cache \
openssh-server~=$SSH_VERSION \
php7-fpm~=$PHP_VERSION \
php7-pdo~=$PHP_VERSION \
php7-pdo_pgsql~=$PHP_VERSION \
php7-bcmath~=$PHP_VERSION \
php7-calendar~=$PHP_VERSION \
php7-curl~=$PHP_VERSION \
php7-dom~=$PHP_VERSION \
php7-fileinfo~=$PHP_VERSION \
php7-gd~=$PHP_VERSION \
php7-iconv~=$PHP_VERSION \
php7-intl~=$PHP_VERSION \
php7-json~=$PHP_VERSION \
php7-mbstring~=$PHP_VERSION \
php7-openssl~=$PHP_VERSION \
php7-session~=$PHP_VERSION \
php7-soap~=$PHP_VERSION \
php7-sodium~=$PHP_VERSION \
php7-tokenizer~=$PHP_VERSION \
php7-xml~=$PHP_VERSION \
php7-xmlwriter~=$PHP_VERSION \
php7-zip~=$PHP_VERSION \
composer~=$COMPOSER_VERSION \
php7-pecl-xdebug~=$XDEBUG_VERSION

RUN ln -s /usr/sbin/php-fpm7 /bin/php-fpm
RUN mkdir /root/.ssh && chmod 0700 /root/.ssh
RUN echo "root:root" | chpasswd

RUN rm -r /etc/php7
COPY etc/ /etc/
COPY bin/* /bin/
RUN chmod +x /bin/*


EXPOSE 9876/tcp
CMD ["php-fpm.sh"]
