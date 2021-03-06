# Docker 镜像源
FROM alpine

# Docker 镜像信息
LABEL MAINTAINER "iLemonrain <ilemonrain@ilemonrain.com>" \
      ARCHITECTURE "amd64"

# Alpine Linux 系统设置
ENV ROOT_PASSWORD="cloudreve"

# Alpine Linux 系统镜像源设置
ENV APK_MIRROR="dl-cdn.alpinelinux.org" \
    APK_MIRROR_SCHEME="http"

# PHP 设置
ENV INSTALL_PHP_EXTENSION="php7-cli php7-json php7-phar php7-mbstring php7-iconv php7-openssl php7-zlib php7-curl php7-fileinfo php7-gd php7-ctype php7-dom php7-simplexml php7-xmlwriter php7-xmlreader php7-mysqli php7-pdo php7-pdo_mysql php7-session"

# Apache2 Web服务器设置
ENV APACHE2_WEB_PORT="80"

# MySQL 数据库设置
ENV MYSQL_URL="localhost" \
    MYSQL_DATABASE="cloudreve_db" \
    MYSQL_PORT="3306" \
    MYSQL_USER="cloudreve" \
    MYSQL_PASSWORD="cloureve" \
    MYSQL_ROOT_PASSWORD="cloudreve"

# Cloudreve 设置
ENV CLOUDREVE_URL="http://localhost:80/"

# ===== 环境安装部分 =====
# 系统基础环境
RUN (sed -i "s/dl-cdn.alpinelinux.org/${APK_MIRROR}/g" /etc/apk/repositories ;\
     sed -i "s/http/${APK_MIRROR_SCHEME}/g" /etc/apk/repositories ;\
     apk --no-cache upgrade ;\
     apk --no-cache add curl git pwgen )

# 安装 Apache2
RUN (apk --no-cache add php7-apache2)

# 安装 PHP 及其扩展
RUN (apk --no-cache add  ${INSTALL_PHP_EXTENSION} ;\
     curl -sS https://getcomposer.org/installer | php ;\
     mv composer.phar /usr/local/bin/composer )

# 安装 MySQL
RUN (apk --no-cache add mysql mysql-client)

# Apache 2 配置
RUN (sed -i "s/AllowOverride None/AllowOverride All/g" /etc/apache2/httpd.conf ;\
     sed -i "/mod_rewrite.so/s/#LoadModule/LoadModule/" /etc/apache2/httpd.conf ;\
     sed -i "s/\/var\/www\/localhost\/htdocs/\/cloudreve/" /etc/apache2/httpd.conf ;\
     mkdir /run/apache2/ )

# 垃圾清理
RUN (rm -rf /var/cache/apk/* /tmp/* ;\
     rm -f /var/www/localhost/htdocs/index.html )

# 添加脚本
ADD scripts/ /scripts/

# 添加网站程序
# ADD wwwroot/ /var/www/localhost/htdocs/

# 配置权限
RUN ( chmod -R 755 /scripts/ )

EXPOSE 80
 
ENTRYPOINT [ "sh", "/scripts/entrypoint.sh" ]
