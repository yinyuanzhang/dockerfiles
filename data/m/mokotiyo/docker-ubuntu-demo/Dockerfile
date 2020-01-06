# ベースとするImage
FROM ubuntu:18.04

# Author
LABEL maintainer="mokotiyo"

# 環境変数
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV TZ 'Asia/Tokyo'

# 対話制御
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update  \
    && apt-get install -y apt-utils  \
    && apt-get install -y apache2 \
        libapache2-mod-php7.2 \
        # composer
        composer \
        # 入れておきたいもの
        vim wget curl make gcc autoconf \
        dnsutils \
        # BEARに必要
        php7.2-xml \
        php7.2-mysql \
        php7.2-mbstring \
        php7.2-curl \
        php7.2-memcached  \
        # 開発でしかいらないパッケージ
        php-xdebug \
    && apt-get clean \
    && echo set encoding=utf-8 > /root/.vimrc

#PHPの設定
RUN phpenmod -s apache2 mbstring

# apacheの設定
RUN a2enmod headers
RUN a2enmod rewrite
RUN a2enmod ssl
RUN a2enmod autoindex
RUN a2dismod mpm_event
RUN a2enmod mpm_prefork

#COPY conf-available/*.conf /etc/apache2/conf-available/
#RUN a2enconf allow_dir
#RUN a2enconf dir
#RUN a2enconf notdirlist
#RUN a2enconf userlog
#RUN a2enconf mpm_prefork

COPY sites-available/*.conf /etc/apache2/sites-available
RUN a2ensite mokotiyo



EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
