FROM josh5/base-ubuntu:16.04
MAINTAINER Josh.5 "jsunnex@gmail.com"


################
### CONFIG:
###
ARG WEBGRIND_VERSION=1.5.0

# Install
RUN \
    echo "**** Install base packages ****" \
        && apt-get update \
        && apt-get install -y --force-yes \
            cron \
            openssl \
            bzip2 \
            nano \
            ca-certificates \
            curl \
            wget \
            software-properties-common \
            dialog \
            htop \
            apt-utils \
            git \
            binutils \
            libstring-shellquote-perl \
            build-essential \
            libfontconfig \
            rsyslog \
            language-pack-en-base \
    && \
    echo "**** Install Apache ****" \
        && apt-get install -y \
            apache2 \
            apache2-bin \
            apache2-data \
            apache2-dev \
            apache2-utils \
    && \
    echo "**** Install RequireJS ****" \
        && apt-get install -y \
            npm \
        && npm install -g requirejs \
    && \
    echo "**** Configure Apache ****" \
        && a2enmod rewrite \
        && a2enmod headers \
        && a2enmod cgi \
        && a2enmod ssl \
        && a2ensite default-ssl \
        && a2dismod mpm_event \
        && a2enmod mpm_prefork \
    && \
    echo "**** Install PHP ****" \
        && export LC_ALL=en_US.UTF-8 \
        && export LANG=en_US.UTF-8 \
        && add-apt-repository -y ppa:ondrej/php \
        && apt-get update \
        && apt-get install -y \
            php5.6 \
            php5.6-bcmath \
            php5.6-cli \
            php5.6-common \
            php5.6-curl \
            php5.6-dom \
            php5.6-fpm \
            php5.6-gd \
            php5.6-json \
            php5.6-ldap \
            php5.6-mbstring \
            php5.6-mcrypt \
            php5.6-mysql \
            php5.6-opcache \
            php5.6-pgsql \
            php5.6-readline \
            php5.6-xml \
            php5.6-xdebug \
            libzend-framework-php \
            zend-framework \
            composer \
    && \
    echo "**** Configure Apache for PHP ****" \
        && a2enmod proxy_fcgi setenvif \
        && a2enconf php5.6-fpm \
    && \
    echo "**** Install Webgrind ****" \
        && apt-get install -y \
            python3 \
            graphviz \
        && \
        rm /usr/bin/python \
        && ln -s /usr/bin/python3 /usr/bin/python \
        && mkdir -p /tools \
        && curl -sSL -o /tmp/webgrind.tar.gz https://github.com/jokkedk/webgrind/archive/v${WEBGRIND_VERSION}.tar.gz \
        && tar zxfp "/tmp/webgrind.tar.gz" -C /tmp \
        && mv /tmp/webgrind-${WEBGRIND_VERSION} /tools/webgrind \
        && chmod +x /tools/webgrind/index.php \
        && sed -i "s#storageDir\ \= ''#storageDir\ \= '/config/log/xdebug'#g" /tools/webgrind/config.php \
        && sed -i "s#profilerDir\ \= '/tmp#profilerDir\ \= '/config/log/xdebug#g" /tools/webgrind/config.php \
    && \
    echo "**** Install phpinfo tool ****" \
        && mkdir -p /tools/phpinfo \
        && echo "<?php phpinfo();" > /tools/phpinfo/index.php \
    && \
    echo "**** Install phpinfo tool ****" \
        && mkdir -p /tools/phpinfo \
        && echo "<?php phpinfo();" > /tools/phpinfo/index.php \
    && \
    echo "**** Copy Default Configs ****" \
        && mkdir -p \
            /defaults/etc/apache2 \
            /defaults/etc/php \
        && cp -rf /etc/apache2/* /defaults/etc/apache2/ \
        && cp -rf /etc/php/* /defaults/etc/php/ \
    && \
    echo "**** cleanup ****" \
        && rm -rf /tmp/* \
        && rm -rf /var/lib/apt/lists/*


# Add local files
COPY root/ /

# environment settings
ENV HOME="/config" \
    INSTALL_NEW=false \
    DEBUGGING_MODULE=false \
    XDEBUG_CONFIG_HOST=localhost \
    XDEBUG_CONFIG_PORT=9000 \
    XDEBUG_CONFIG_IDEKEY=PHPSTORM \
    PATH="$HOME/.composer/vendor/bin/:${PATH}" \
    COMPOSER_HOME=/config/.composer



# intended ports and volumes
EXPOSE 22 80 443
VOLUME /config