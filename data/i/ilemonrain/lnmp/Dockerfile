FROM alpine

LABEL MAINTAINER="iLemonrain <ilemonrain@ilemonrain.com>" \
      ARCHITECTURE="x86_64"

ENV INSTALL_PHP7_EXTENSION="php7-fpm php7-mysqli php7-json php7-openssl php7-curl php7-zlib php7-xml php7-phar php7-intl php7-dom php7-xmlreader php7-ctype php7-mbstring php7-gd"

# MySQL 数据库设置
ENV MYSQL_URL="localhost" \
    MYSQL_DATABASE="docker_lnmp_db" \
    MYSQL_PORT="3306" \
    MYSQL_USER="docker_lnmp" \
    MYSQL_PASSWORD="docker_lnmp" \
    MYSQL_ROOT_PASSWORD="docker_lnmp"

# 系统核心升级
RUN (apk --no-cache upgrade )

# 系统基础组件
RUN (apk --no-cache add curl )

# PHP 7
RUN (apk --no-cache add php7 ${INSTALL_PHP7_EXTENSION} )

# Nginx
RUN (apk --no-cache add nginx )

# MariaDB (MySQL)
RUN (apk --no-cache add mysql mysql-client)

# 导入Nginx配置文件
COPY config/nginx.conf /etc/nginx/nginx.conf

# 导入PHP 7配置文件
COPY config/php-fpm-pool.conf /etc/php7/php-fpm.d/docker_lnmp_custom.conf
COPY config/php.ini /etc/php7/conf.d/docker_lnmp_custom.ini

# 添加网站
COPY wwwroot/ /www/

COPY scripts/entrypoint.sh /scripts/entrypoint.sh

# 处理权限
RUN (chmod -R 755 /www ;\
     chown -R nginx:nginx /www )

EXPOSE 80 443

VOLUME [ "/www" ]

CMD [ "sh", "/scripts/entrypoint.sh"]