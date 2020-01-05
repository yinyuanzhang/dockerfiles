# 使用官方 PHP-Apache 镜像
FROM php:apache

# docker-php-ext-install 为官方 PHP 镜像内置命令，用于安装 PHP 扩展依赖
# pdo_mysql 为 PHP 连接 MySQL 扩展
RUN docker-php-ext-install pdo_mysql
RUN docker-php-ext-install mysqli
# RUN docker-php-ext-install rewrite

RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y
RUN apt-get install vim -y

RUN a2enmod rewrite && service apache2 restart