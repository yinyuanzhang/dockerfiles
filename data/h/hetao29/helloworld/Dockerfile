FROM alpine:3.9
LABEL maintainer="Hetao<hetao@hetao.name>"
VOLUME ["/data/volume"]
RUN buildDeps='nginx php7-fpm php7-imap php7-mbstring php7-json php7-curl php7-common php7-ldap php7-pecl-redis php7-pecl-mcrypt php7-ldap php7-pdo_mysql php7-mysqlnd php7-mysqli php7-bcmath php7-curl php7-opcache php7-gd php7-xml php7-simplexml' \
    && sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk update \
    && apk add $buildDeps  \ 
    && mkdir -p /data/bin \
    && mkdir -p /data/etc/nginx \
    && mkdir -p /data/php/wwwroot \
    && cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak \
    && cp /etc/php7/php.ini /etc/php7/php.ini.bak \
    && cp /etc/php7/php-fpm.conf  /etc/php7/php-fpm.conf.bak \
    && cp /etc/php7/php-fpm.d/www.conf /etc/php7/php-fpm.d/www.conf.bak

COPY src/start.sh /data/bin/
COPY src/nginx/nginx.conf /etc/nginx/
COPY src/fpm/php.ini /etc/php7/php.ini
COPY src/fpm/php-fpm.conf /etc/php7/php-fpm.conf
COPY src/fpm/pool.d/www.conf /etc/php7/php-fpm.d/www.conf
COPY src/php/* /data/php/wwwroot/
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log && ln -sf /dev/stdout /var/log/php-fpm.log && ln -sf /dev/stdout /var/log/php-fpm-slow.log
EXPOSE 80:80 443:443
CMD ["/bin/sh","/data/bin/start.sh"]
