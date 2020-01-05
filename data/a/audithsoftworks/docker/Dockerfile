FROM php:7.3-fpm
LABEL maintainer="Shahriyar Imanov <shehi@imanov.me>"

WORKDIR /var/www

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y \
    && apt-get install -y apt-utils \
    && apt-get upgrade -y \
    && mkdir -p /usr/share/man/man1 \
    && apt-get install -y \
        bzip2 \
        cron \
        daemon \
        fontforge \
        git \
        gnupg \
        iputils-ping \
#        libsqlite3-dev \
#        libssl-dev \
        locales \
        locales-all \
        mariadb-client \
        nano \
        openjdk-11-jre \
        procps \
        rsyslog \
        sudo \
        telnet \
        unzip \
        wget

# Locale
RUN locale-gen en_US.UTF-8 && locale-gen de_DE.UTF-8 && dpkg-reconfigure locales
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install PHP extensions
RUN docker-php-ext-install \
        bcmath \
        calendar \
        exif \
        gettext \
        pdo_mysql \
        sockets

RUN apt-get install -y libfreetype6-dev libjpeg-dev libjpeg62-turbo-dev libpng-dev \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include \
    && docker-php-ext-install gd

RUN apt-get install -y libicu-dev && docker-php-ext-install intl

RUN apt-get install -y libmcrypt-dev libmemcached-dev \
    && pecl install -of mcrypt memcached \
    && docker-php-ext-enable mcrypt memcached

RUN apt-get install -y libpq-dev && docker-php-ext-install pdo_pgsql

RUN apt-get install -y libxml2-dev && docker-php-ext-install soap

RUN apt-get install -y libxslt1-dev && docker-php-ext-install xsl

RUN apt-get install -y libzip-dev && docker-php-ext-install zip

# Install Google's depot-tools
#RUN apt-get install -y python libglib2.0-dev
#RUN git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git /tmp/.depot-tools
#ENV PATH=$PATH:/tmp/.depot-tools

# Fetch and compile v8
#RUN cd /tmp \
#    && fetch v8 \
#    && cd v8 \
#    && git checkout 6.4.345 \
#    && gclient sync \
#    && tools/dev/v8gen.py -vv x64.release -- is_component_build=true \
#    && ninja -C out.gn/x64.release/ \
#    && mkdir -p /opt/v8/lib \
#    && mkdir -p /opt/v8/include \
#    && cp out.gn/x64.release/lib*.so out.gn/x64.release/*_blob.bin out.gn/x64.release/icudtl.dat /opt/v8/lib/ \
#    && cp -R include/* /opt/v8/include/ \
#    && apt-get remove python -y

# Compile php-v8js
#RUN git clone --depth=1 https://github.com/phpv8/v8js.git /tmp/v8js \
#    && cd /tmp/v8js \
#    && phpize \
#    && ./configure --with-v8js=/opt/v8 LDFLAGS="-lstdc++"
#ENV NO_INTERACTION 1
#RUN cd /tmp/v8js \
#    && make \
#    && make test \
#    && make install \
#    && docker-php-ext-enable v8js

# Install PECL php-mongodb
RUN pecl install -of mongodb \
    && rm -rf /tmp/pear \
    && echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/mongo.ini

# Install PECL php-xdebug
RUN pecl install -of xdebug \
    && rm -rf /tmp/pear \
    && echo "zend_extension=xdebug.so" | tee /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.max_nesting_level = 1000" | tee -a /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.idekey = basisPhp" | tee -a /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_enable = 1" | tee -a /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_port = 54321" | tee -a /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_connect_back = 1" | tee -a /usr/local/etc/php/conf.d/xdebug.ini

# Port for XDebug
EXPOSE 54321

# Timezone
RUN echo "date.timezone = UTC" | tee /usr/local/etc/php/conf.d/date.ini

# Install php-redis extension through Git
RUN git clone https://github.com/phpredis/phpredis.git /tmp/phpredis \
    && cd /tmp/phpredis \
    && git checkout 5.1.1 \
    && phpize \
    && ./configure \
    && make \
    && make install \
    && echo "extension=redis.so" | tee /usr/local/etc/php/conf.d/redis.ini

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer
RUN composer global require hirak/prestissimo

# Some checks
RUN service rsyslog start && service cron start && service --status-all
RUN php -m

# Install Node
RUN set -ex \
    && for key in \
        94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
        FD3A5288F042B6850C66B31F09FE44734EB7990E \
        71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
        DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
        C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
        B9AE9905FFD7803F25714661B63B535A4C206CA9 \
        77984A986EBC2AA786BC0F66B01FBB92821C587A \
        8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600 \
        4ED778F539E3634C779C87C6D7062848A1AB005C \
        A48C2BEE680E841632CD4E44F07496B3EB3C1762 \
        B9E2F5981AA6E0CD28160D9FF13993A75599653C \
    ; do \
        gpg --batch --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \
        gpg --batch --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \
        gpg --batch --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \
    done

ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 12.13.0
ENV NPM_VERSION 6
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
    && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
    && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
    && grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
    && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
    && rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
    && ln -s /usr/local/bin/node /usr/local/bin/nodejs \
    && npm install -g npm@$NPM_VERSION \
    && rm -rf /tmp/npm-*

# Install Node global dependencies
RUN npm install -g ttf2eot jshint webpack webpack-cli prettier mocha

# Port for node --inspect
EXPOSE 9229

# Install fonting tools
RUN apt-get update -y && apt-get install woff-tools \
    && git clone --depth=1 https://github.com/google/woff2.git /opt/woff2 \
    && cd /opt/woff2 \
    && git submodule init \
    && git submodule update \
    && make clean all \
    && chmod +x /opt/woff2/woff2_* \
    && git clone --depth=1 https://github.com/zoltan-dulac/css3FontConverter.git /opt/css3_font_converter \
    && chmod +x /opt/css3_font_converter/convertFonts.sh;

# Install Cypress dependencies
RUN apt-get update -y \
    && apt-get install -y \
        libasound2 \
        libgconf-2-4 \
        libgtk-3-dev \
        libnotify-dev \
        libnss3 \
        libxss1 \
        xvfb

# Install Chrome browser
RUN \
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list
RUN apt-get update
# disabled dbus install - could not get it to install
# but tested an example project, and Chrome seems to run fine
# RUN apt-get install -y dbus-x11
RUN apt-get install -y google-chrome-stable
RUN rm -rf /var/lib/apt/lists/*

# "Fake" dbus address to prevent errors
# https://github.com/SeleniumHQ/docker-selenium/issues/87
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

# Install Firefox browser
ARG FIREFOX_VERSION=70.0.1
RUN wget --no-verbose -O /tmp/firefox.tar.bz2 https://download-installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-US/firefox-$FIREFOX_VERSION.tar.bz2 \
  && tar -C /opt -xjf /tmp/firefox.tar.bz2 \
  && rm /tmp/firefox.tar.bz2 \
  && ln -fs /opt/firefox/firefox /usr/bin/firefox

# Clean-up
RUN apt-get clean \
    && apt-get remove -y gnupg \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add a non-root user to prevent files being created with root permissions on host machine.
ARG PUID=1000
ARG PGID=1000
RUN groupadd -g $PGID audith && useradd -u $PUID -g audith -M audith
RUN usermod -aG sudo audith
RUN sed -i -e "s/%sudo.*/%sudo ALL=(ALL:ALL) NOPASSWD: ALL/g" /etc/sudoers

COPY ./profile /etc/profile
COPY ./profile /etc/bashrc

USER audith

# Update PATH
ENV PATH $PATH:/opt/woff2:/opt/css3_font_converter
