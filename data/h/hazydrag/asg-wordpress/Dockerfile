#
# Dockerfile for WordPress
#
FROM appsvcorg/nginx-fpm:php7.3.4-redis
LABEL MAINTAINER Azure App Service Container Images <appsvc-images@microsoft.com>
# ========
# ENV vars
# ========
# ssh
ENV SSH_PASSWD "root:Docker!"
ENV SSH_PORT 2222
#nginx
ENV NGINX_LOG_DIR "/home/LogFiles/nginx"
#php
ENV PHP_HOME "/usr/local/etc/php"
ENV PHP_CONF_DIR $PHP_HOME
ENV PHP_CONF_FILE $PHP_CONF_DIR"/php.ini"
# mariadb
ENV MARIADB_DATA_DIR "/home/data/mysql"
ENV MARIADB_LOG_DIR "/home/LogFiles/mysql"
# phpmyadmin
ENV PHPMYADMIN_SOURCE "/usr/src/phpmyadmin"
ENV PHPMYADMIN_HOME "/home/phpmyadmin"
# wordpress
ENV WORDPRESS_SOURCE "/usr/src/wordpress"
ENV WORDPRESS_HOME "/home/site/wwwroot"
#
ENV DOCKER_BUILD_HOME "/dockerbuild"
# ====================
# ====================
# wordpress
COPY wordpress_src/. $WORDPRESS_SOURCE/
# supervisor
COPY supervisord.conf /etc/
# php
COPY uploads.ini /usr/local/etc/php/conf.d/
# nginx
COPY nginx_conf/. /etc/nginx/conf.d/
# newrelict
RUN \
  curl -L http://download.newrelic.com/php_agent/release/newrelic-php5-8.7.0.242-linux-musl.tar.gz | tar -C /tmp -zx && \
   export NR_INSTALL_USE_CP_NOT_LN=1 && \
    export NR_INSTALL_SILENT=1 && \
     /tmp/newrelic-php5-*/newrelic-install install && \
      rm -rf /tmp/newrelic-php5-* /tmp/nrinstall* && \
        sed -i -e 's/"REPLACE_WITH_REAL_KEY"/"052a228fd1bc49d2f6766ba79151bd05648555c5"/' \
     -e 's/newrelic.appname = "PHP Application"/newrelic.appname = "TimbavatiLodges"/' \
         /usr/local/etc/php/conf.d/newrelic.ini
#
COPY local_bin/. /usr/local/bin/
RUN chmod -R +x /usr/local/bin
EXPOSE $SSH_PORT 80
ENTRYPOINT ["entrypoint.sh"]
