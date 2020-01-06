# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.

# TODO: how to hand mail send.

# APPLARI/PHUSION-NGINX-PHP7-MARIADB

FROM phusion/baseimage:0.9.21

MAINTAINER Esa Heiskanen <esa@applari.fi>

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

ARG NGINX_VERSION=1.13.0
ARG NAXSI_VERSION=0.55.3
ARG PAGESPEED_VERSION=1.12.34.2
ARG PHP_VERSION=7.1
ARG DEBIAN_FRONTEND=noninteractive
ARG WPCLI_CONFIG_PATH=/var/www/wp-cli.yml
ENV WPCLI_CONFIG_PATH=${WPCLI_CONFIG_PATH}

# Ensure UTF-8
RUN locale-gen                  en_US.UTF-8 && \
    locale-gen                  fi_FI.UTF-8 && \
    ln -snf /usr/share/zoneinfo/Europe/Helsinki /etc/localtime && \
    echo Europe/Helsinki > /etc/timezone

ENV LANG=en_GB.utf8 \
    LC_CTYPE=fi_FI.utf8 \
    LC_NUMERIC=fi_FI.utf8 \
    LC_TIME=fi_FI.utf8 \
    LC_COLLATE=fi_FI.utf8 \
    LC_MONETARY=fi_FI.utf8 \
    LC_MESSAGES=fi_FI.utf8 \
    LC_PAPER=fi_FI.utf8 \
    LC_NAME=fi_FI.utf8 \
    LC_ADDRESS=fi_FI.utf8 \
    LC_TELEPHONE=fi_FI.utf8 \
    LC_MEASUREMENT=fi_FI.utf8 \
    LC_IDENTIFICATION=fi_FI.utf8 \
    LC_ALL=fi_FI.utf8 \
    TERM=xterm \
    HOME=/root \
    WP_CLI_CONFIG_PATH=$WPCLI_CONFIG_PATH


# generate keypair and Disable SSH (Not using it at the moment).
RUN ssh-keygen -t rsa -N "" -f /root/.ssh/id_rsa

# generate keypair
#RUN /etc/my_init.d/00_regen_ssh_host_keys.sh
    #disable ssh
    #rm -rf /etc/service/sshd && \

### INIT package manager \


RUN add-apt-repository ppa:ondrej/php && \
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && \
	apt-get clean && apt-get update && apt-get update && apt-get -y upgrade && \
    apt-get install -qy tar git vim nano wget net-tools build-essential unzip\
    libpcre3-dev libxslt1-dev libgd2-xpm-dev libgeoip-dev libssl-dev zlib1g-dev libpcre3 libpcre3-dev\
    mariadb-server mariadb-client \
    php$PHP_VERSION php$PHP_VERSION-fpm php$PHP_VERSION-common php$PHP_VERSION-cli php$PHP_VERSION-mysqlnd php$PHP_VERSION-mcrypt php$PHP_VERSION-curl php$PHP_VERSION-bcmath php$PHP_VERSION-mbstring php$PHP_VERSION-soap php$PHP_VERSION-xml php$PHP_VERSION-zip php$PHP_VERSION-json php$PHP_VERSION-imap php-xdebug \
    git git-lfs php-imagick 

# Get nginx and modules source and compile
RUN cd /tmp/ && \
    # NGINX source \
    wget https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz && \
    # Naxsi sources \
    wget https://github.com/nbs-system/naxsi/archive/$NAXSI_VERSION.tar.gz && \
    tar xf $NAXSI_VERSION.tar.gz && \
    tar xf nginx-$NGINX_VERSION.tar.gz && \
    # Pagespeed
    wget https://github.com/pagespeed/ngx_pagespeed/archive/v${PAGESPEED_VERSION}-beta.zip && \
    unzip v${PAGESPEED_VERSION}-beta.zip && \
    cd ngx_pagespeed-${PAGESPEED_VERSION}-beta && \
    psol_url=https://dl.google.com/dl/page-speed/psol/${PAGESPEED_VERSION}.tar.gz && \
    [ -e scripts/format_binary_url.sh ] && psol_url=$(scripts/format_binary_url.sh PSOL_BINARY_URL) && \
    wget ${psol_url} && \
    tar -xzvf $(basename ${psol_url}) && \
    cd .. && \

    # Compile \
    cd nginx-$NGINX_VERSION && \
    ./configure --conf-path=/etc/nginx/nginx.conf \
        --add-module=../naxsi-$NAXSI_VERSION/naxsi_src \
        --add-module=../ngx_pagespeed-${PAGESPEED_VERSION}-beta ${PS_NGX_EXTRA_FLAGS} \
        --error-log-path=/var/log/nginx/error.log \
        --http-client-body-temp-path=/var/lib/nginx/body \
        --http-fastcgi-temp-path=/var/lib/nginx/fastcgi \
        --http-log-path=/var/log/nginx/access.log \
        --http-proxy-temp-path=/var/lib/nginx/proxy \
        --lock-path=/var/lock/nginx.lock \
        --pid-path=/var/run/nginx.pid \
        --prefix=/usr \
        # include modules \
        --with-http_ssl_module \
        --with-http_geoip_module \
        --with-http_gzip_static_module \
        #--with-http_spdy_module \
        --with-ipv6 \
        # exclude modules \
        --without-mail_pop3_module \
        --without-mail_smtp_module \
        --without-mail_imap_module \
        --without-http_uwsgi_module \
        --without-http_scgi_module && \
    make && \
    make install && \
    mkdir -p /var/lib/nginx/{body,proxy}

COPY build/nginx.conf /etc/nginx/

# COPY run script
COPY build/nginx.sh /etc/service/02_nginx/run

### PHP7-FPM
# nginx-php installation

COPY build/php.ini /etc/php/7.1/fpm/
COPY build/php-fpm.conf /etc/php/7.1/fpm/
# generate a simple index file with phpinfo
#COPY build/nginx-default.conf /etc/nginx/sites-available/default/
COPY build/test.php /root/dockerscripts/
#RUN sed -i 's#%%php_fpm_sock_file%%#/run/php/php7.1-fpm.sock#g' /etc/nginx/sites-available/default &&
#RUN echo "<?php\nphpinfo();">/var/www/html/index.php

# create /run/php/php7.1-fpm.pid file by starting and stopping service
# https://serverfault.com/questions/786398/how-do-i-start-php7.1-fpm-with-supervisord
COPY build/php-fpm.sh /etc/service/01_php-fpm/run


# Tweak my.cnf
#RUN sed -i -e 's#\(bind-COPYress.*=\).*#\1 0.0.0.0#g' /etc/mysql/my.cnf
#RUN sed -i -e 's#\(log_error.*=\).*#\1 /db/mysql_safe.log#g' /etc/mysql/my.cnf
#RUN sed -i -e 's/\(user.*=\).*/\1 nobody/g' /etc/mysql/my.cnf

#RUN echo 'socket=/tmp/mysql.sock' >> /etc/mysql/my.cnf
#RUN echo 'port=3306' >> /etc/mysql/my.cnf

# COPY mariadb to runit
#RUN mkdir /etc/service/mariadb
COPY build/mariadb.sh /etc/service/03_mariadb/run

# add mariadb configs
COPY build/applari-mysql.cnf /etc/mysql/conf.d/

# RUN echo '[mysqld]' > /etc/mysql/conf.d/applari.cnf && \
#     echo 'innodb_file_per_table' >> /etc/mysql/conf.d/applari.cnf && \
#     echo 'general_log_file = /var/log/mysql/mysql.log' >> /etc/mysql/conf.d/applari.cnf && \
#     echo 'general_log = 1' >> /etc/mysql/conf.d/applari.cnf && \
#     echo 'log_warnings = 2' >> /etc/mysql/conf.d/applari.cnf && \
    ### install wp-cli
RUN cd ~  && \
    curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
    php wp-cli.phar --info --allow-root && \
    chmod +x wp-cli.phar && \
	mv wp-cli.phar /usr/local/bin/wp && \
    echo "alias wp='/usr/local/bin/wp --allow-root '" >> /root/.bashrc && \
    mkdir -p /var/www/ && test -e "${WPCLI_CONFIG_PATH}" && echo "${WPCLI_CONFIG_PATH} found" || touch "${WPCLI_CONFIG_PATH}" && echo "path: /var/www/html/" >> "${WPCLI_CONFIG_PATH}" && echo "color: auto" >> "${WPCLI_CONFIG_PATH}" && \
    # Installing WordPress Bash Completions \
    cd /tmp/ && \
    curl -O https://raw.githubusercontent.com/wp-cli/wp-cli/master/utils/wp-completion.bash && \
    chmod +x wp-completion.bash && \
    mv wp-completion.bash /usr/local/etc/bash_completion.d && \
    # install pagespeed module for nginx

    # remove services \
    service php7.1-fpm start && service php7.1-fpm stop && \
    update-rc.d -f nginx remove && update-rc.d -f php7.1-fpm remove && update-rc.d -f mysql remove && \
    # fix permissions \
    chmod +x /etc/service/01_php-fpm/run && \
    chmod +x /etc/service/02_nginx/run && \
    chmod +x /etc/service/03_mariadb/run && \
    # clean up APT when done. \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /bd_build

COPY scripts/installwp.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/installwp.sh

COPY scripts/fastcgi_cache.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/fastcgi_cache.sh

COPY scripts/check-docker-config.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/check-docker-config.sh

# ADD https://wordpress.org/latest.tar.gz /var/www/html/

# run startup scripts https://github.com/phusion/baseimage-docker#running_startup_scripts
RUN mkdir -p /etc/my_init.d
# sample COPY logtime.sh /etc/my_init.d/logtime.sh
# sample RUN chmod +x /etc/my_init.d/logtime.sh

VOLUME /var/www/
VOLUME /var/lib/mysql/

# port and settings
EXPOSE 80:80 443:443 3306

WORKDIR /var/www/html/
