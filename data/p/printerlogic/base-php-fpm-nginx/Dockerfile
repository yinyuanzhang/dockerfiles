FROM php:7.0.27-fpm

# Versions of major apps
ENV COMPOSER_VERSION=1.5.6 \
    GOSU_VERSION=1.10 \
    NGINX_VERSION=1.12.2-1~jessie \
    NJS_VERSION=1.12.2.0.1.14-1~jessie \
    NODE_VERSION=8.11.3

# other settings
ENV NPM_CONFIG_LOGLEVEL=info

# umask fix
RUN sed -i 's|^UMASK[[:space:]]\+022$|UMASK 002|' /etc/login.defs
RUN umask 0002

# UPDATED GOSU INSTALL BASED ON SEVERAL FIXES FOUND IN:
# https://raw.githubusercontent.com/jacobalberty/unifi-docker/599dff10e60ab13796e97fba21a3ac0b45ddaacd/Dockerfile
# Install gosu
# https://github.com/tianon/gosu/blob/master/INSTALL.md
# This should be integrated with the main run because it duplicates a lot of the steps there
# but for now while shoehorning gosu in it is seperate
RUN set -ex \
    && fetchDeps=' \
        ca-certificates \
        dirmngr \
        wget \
    ' \
    && apt-get update \
    && apt-get install -y --no-install-recommends $fetchDeps \
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
# verify the signature
    && export GNUPGHOME="$(mktemp -d)" \
    && for server in $(shuf -e ha.pool.sks-keyservers.net \
                            hkp://p80.pool.sks-keyservers.net:80 \
                            keyserver.ubuntu.com \
                            hkp://keyserver.ubuntu.com:80 \
                            pgp.mit.edu) ; do \
        gpg --keyserver "$server" --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 && break || : ; \
    done \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
# verify that the binary works
    && gosu nobody true \
    && apt-get purge -y --auto-remove $fetchDeps \
    && rm -rf /var/lib/apt/lists/*

# install apt dependencies
RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y \
    ca-certificates \
    curl \ 
    dos2unix \
    git \
    g++ \
    jq \
    ldap-utils=2.4.40+dfsg-1+deb8u3 \
    libc-client2007e=8:2007f~dfsg-4 \
    libc-client-dev \
    libkrb5-dev=1.12.1+dfsg-19+deb8u4 \
    libedit-dev=3.1-20140620-2 \
    libfcgi0ldbl=2.4.0-8.3 \
    libfreetype6-dev=2.5.2-3+deb8u2 \
    libicu-dev=52.1-8+deb8u7 \
    libjpeg62-turbo-dev=1:1.3.1-12 \
    libldap2-dev=2.4.40+dfsg-1+deb8u3 \
    libmcrypt-dev=2.5.8-3.3 \
    libpng12-dev=1.2.50-2+deb8u3 \
    libpq-dev=9.4.19-0+deb8u1 \
    libssl-dev=1.0.1t-1+deb8u9 \
    libsnmp-dev=5.7.2.1+dfsg-1+deb8u2 \
    libxext6=2:1.3.3-1 \
    libxrender1=1:0.9.8-1+b1 \
    locales \
    mcrypt=2.6.8-1.3 \
    mysql-client \
    openssh-client \
    rsync \
    snmp \
    sqlite3 \
    supervisor \
    unzip \
    vim \
    zip \
    && rm -r /var/lib/apt/lists/*
#gnupg1 \
# Patrick Miller Jan 2018 Added libxext, libxrender for wkhtmltopdf package
# Patrick Miller Feb 2018 Added libc-client-dev (libc-client2007e), libkrb5-dev for php imap extension

# help docker-php-ext-install find ldap libs
RUN ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so \
    && ln -s /usr/lib/x86_64-linux-gnu/liblber.so /usr/lib/liblber.so

# configure imap
RUN docker-php-ext-configure imap --with-imap --with-imap-ssl --with-kerberos

# configure ldap
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/

# configure intl
RUN docker-php-ext-configure intl

# configure gd
RUN docker-php-ext-configure gd \
    --enable-gd-native-ttf \
    --with-freetype-dir=/usr/include/freetype2 \
    --with-jpeg-dir=/usr/include/

# Install extensions using the helper script provided by the base image
RUN docker-php-ext-install \
    gd \
    imap \
    intl \
    json \
    ldap \
    mcrypt \
    mysqli \
    pdo_mysql \
    readline \
    snmp \
    zip

# Install and configure xdebug
ENV XDEBUG_ENABLED=0 \
    XDEBUG_AUTOSTART=off \
    XDEBUG_CONF_FILE=docker-php-ext-xdebug.ini \
    XDEBUG_CONNECT_BACK_PORT=9000 \
    XDEBUG_CONNECT_BACK=0 \
    XDEBUG_REMOTE_HOST=localhost \
    XDEBUG_REMOTE_LOG=/var/www/app/storage/logs/xdebug.log \
    FASTCGI_READ_TIMEOUT=60s

# install xdebug, setup environment variables, and create xdebug enablement script
RUN docker-php-source extract \
    && pecl install xdebug \
    && docker-php-ext-enable xdebug \
    && docker-php-source delete \
    && mkdir -p "${PHP_INI_DIR}/../mods-available" \
    && mv "${PHP_INI_DIR}/conf.d/${XDEBUG_CONF_FILE}" "${PHP_INI_DIR}/../mods-available" \
    && { \
        echo ""; \
        echo "[xdebug]"; \
        echo "xdebug.remote_enable = ${XDEBUG_ENABLED}"; \
        echo "xdebug.remote_autostart = ${XDEBUG_AUTOSTART}"; \
        echo "xdebug.remote_connect_back = ${XDEBUG_CONNECT_BACK}"; \
        echo "xdebug.remote_host = ${XDEBUG_REMOTE_HOST}"; \
        echo "xdebug.remote_port = ${XDEBUG_CONNECT_BACK_PORT}"; \
        echo "xdebug.remote_log = ${XDEBUG_REMOTE_LOG}"; \
        echo "xdebug.remote_handler = dbgp"; \
        echo "xdebug.max_nesting_level = 1000"; \
    } >> "${PHP_INI_DIR}/../mods-available/${XDEBUG_CONF_FILE}"

COPY  enable-debugger.sh  /usr/local/bin/enable-debugger
RUN chmod +x /usr/local/bin/enable-debugger

# Add Ldap env variables
RUN sed -i '$a\
TLS_REQCERT never \
' /etc/ldap/ldap.conf

# Generate all locales and set default locale
# @TODO We probably do not need ALL of the locales, 471 languages
RUN tail -n +5 /etc/locale.gen | cut -c 3- > /etc/locale_new.gen
RUN rm /etc/locale.gen
RUN mv /etc/locale_new.gen /etc/locale.gen
RUN dpkg-reconfigure --frontend=noninteractive locales
RUN update-locale LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8 LC_CTYPE=UTF-8 LANG=en_US.UTF-8

# Install dev certificates
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/ssl-cert-snakeoil.key -out /etc/ssl/certs/ssl-cert-snakeoil.pem -subj "/C=US/ST=Utah/L=St George/O=PrinterLogic/CN=*.pl-local.com"

# install nginx
RUN NGINX_GPGKEY=573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62; \
	found=''; \
	for server in \
		ha.pool.sks-keyservers.net \
		hkp://keyserver.ubuntu.com:80 \
		hkp://p80.pool.sks-keyservers.net:80 \
		pgp.mit.edu \
	; do \
		echo "Fetching GPG key $NGINX_GPGKEY from $server"; \
		apt-key adv --keyserver "$server" --keyserver-options timeout=10 --recv-keys "$NGINX_GPGKEY" && found=yes && break; \
	done; \
	test -z "$found" && echo >&2 "error: failed to fetch GPG key $NGINX_GPGKEY" && exit 1; \
	echo "deb http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
						nginx=${NGINX_VERSION} \
						nginx-module-xslt=${NGINX_VERSION} \
						nginx-module-geoip=${NGINX_VERSION} \
						nginx-module-image-filter=${NGINX_VERSION} \
						nginx-module-njs=${NJS_VERSION} \
						gettext-base \
	&& rm -rf /var/lib/apt/lists/*

# forward nginx request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

# install composer so we can run dump-autoload at startup
ENV PATH="/composer/vendor/bin:$PATH" \
    COMPOSER_ALLOW_SUPERUSER=1 \
    COMPOSER_VENDOR_DIR=/var/www/vendor \
    COMPOSER_HOME=/composer
RUN curl -s -f -L -o /tmp/installer.php https://raw.githubusercontent.com/composer/getcomposer.org/da290238de6d63faace0343efbdd5aa9354332c5/web/installer \
 && php -r " \
    \$signature = '669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410'; \
    \$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \
    if (!hash_equals(\$signature, \$hash)) { \
        unlink('/tmp/installer.php'); \
        echo 'Integrity check failed, installer is either corrupt or worse.' . PHP_EOL; \
        exit(1); \
    }" \
 && php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer --version=${COMPOSER_VERSION} \
 && rm /tmp/installer.php \
 && composer --ansi --version --no-interaction

# install node for running gulp at container startup
# gpg keys listed at https://github.com/nodejs/node#release-team
RUN set -ex \
    && for key in \
        94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
        FD3A5288F042B6850C66B31F09FE44734EB7990E \
        71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
        DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
        C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
        B9AE9905FFD7803F25714661B63B535A4C206CA9 \
        56730D5401028683275BD23C23EFEFE93C4CFFFE \
        77984A986EBC2AA786BC0F66B01FBB92821C587A \
        8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600 \
    ; do \
        gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \
        gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \
        gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \
    done

RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \
  && case "${dpkgArch##*-}" in \
    amd64) ARCH='x64';; \
    ppc64el) ARCH='ppc64le';; \
    s390x) ARCH='s390x';; \
    arm64) ARCH='arm64';; \
    armhf) ARCH='armv7l';; \
    *) echo "unsupported architecture"; exit 1 ;; \
  esac \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH.tar.xz" \
  && curl -SLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
  && tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

ENV PATH /var/www/node_modules/.bin:$PATH

COPY ./config/supervisord.conf /etc/supervisor/supervisord.conf

CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]