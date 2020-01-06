FROM php:7.1-fpm
MAINTAINER markoos <sergey.semenyuk@gen.tech>

ENV NR_INSTALL_SILENT 1
ENV NR_INSTALL_KEY e78318736324bb6aaeefc03ef325e825e23d5b3b
ENV NR_APP_NAME ""
ENV NEWRELIC_VERSION 6.8.0.177

ENV APP_ENV prod
############################## PHP-FPM ##############################################
RUN apt-get update && apt-get install procps rsyslog net-tools htop vim telnet wget git-core zip unzip \
        #for nginx
        libpcre3 libpcre3-dev libssl-dev libgeoip-dev autoconf make build-essential \
        #for mozjpeg
        nasm autogen automake autotools-dev libtool \
        libfreetype6-dev libjbig-dev libpng-dev libjpeg62-turbo-dev libjpeg-dev \
        libexif-dev \
        gnupg \
        gnupg2 \
        gnupg-agent \
        ffmpeg graphicsmagick -y   \
        #for Pillow-SIMD
        python-pip python-dev python-setuptools && \
        pip install -U --force-reinstall pillow-simd && \
        php -r "readfile('http://getcomposer.org/installer');" | php -- --install-dir=/usr/bin/ --filename=composer && \
        docker-php-ext-install exif

################## nginx #########################
ARG NGINX_VERSION
ENV NGINX_VERSION ${NGINX_VERSION:-1.12.2}

RUN mkdir -p /tmp/nginx \
    && git clone git://github.com/mailru/graphite-nginx-module /tmp/graphite-nginx-module \
    && wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz -O - | tar -zxf - -C /tmp/nginx --strip=1 \
    && cd /tmp/nginx \
    && patch -p1 < /tmp/graphite-nginx-module/graphite_module_v1_7_7.patch && ./configure \
--prefix=/usr/share/nginx \
--sbin-path=/usr/sbin \
--conf-path=/etc/nginx/nginx.conf \
--lock-path=/var/lock/nginx.lock \
--pid-path=/var/run/nginx.pid \
--error-log-path=/var/log/nginx/error.log \
--http-log-path=/var/log/nginx/access.log \
--add-module=/tmp/graphite-nginx-module \
--with-http_ssl_module \
--with-http_addition_module \
--with-http_auth_request_module \
--with-http_geoip_module \
--with-http_realip_module \
--with-http_v2_module \
--with-http_mp4_module \
--with-http_slice_module \
--with-http_sub_module \
--with-http_gzip_static_module \
--with-http_stub_status_module \
&& make && make install

###===--- Supervisor
ENV SUPERVISOR_VERSION 3.3.3
RUN apt-get install --force-yes python-pip -y \
    && pip install supervisor==$SUPERVISOR_VERSION \
    && mkdir -p /etc/supervisor/conf.d \
    && mkdir -p /var/log/supervisor 

COPY supervisord.conf /etc/supervisor/

## GM 
WORKDIR /tmp/
ENV mozjpeg 3.2
RUN wget https://github.com/mozilla/mozjpeg/releases/download/v$mozjpeg/mozjpeg-$mozjpeg-release-source.tar.gz \
    && tar zxvf mozjpeg-$mozjpeg-release-source.tar.gz \
    && cd /tmp/mozjpeg; autoreconf -fiv; ./configure \
    && make && make install \
    && cp /opt/mozjpeg/bin/cjpeg /usr/local/bin/

ENV libwebp 0.6.0
RUN wget https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-$libwebp.tar.gz \
    && tar -xvf libwebp-$libwebp.tar.gz \
    && cd /tmp/libwebp-$libwebp \
    && ./configure \
    && make && make install \
    && ranlib /usr/local/lib/libwebp.a && ldconfig /usr/local/lib

RUN git clone --recursive https://github.com/pornel/pngquant.git \
    && cd /tmp/pngquant \
    && make && make install

# GraphicsMagick
ENV GM 1.3.26
RUN wget https://sourceforge.net/projects/graphicsmagick/files/graphicsmagick/$GM/GraphicsMagick-$GM.tar.gz \
    && tar zxvf GraphicsMagick-$GM.tar.gz \
    && cd /tmp/GraphicsMagick-$GM \
    && ./configure \
    && make && make install

#CLEAN
RUN apt-get clean && rm -rf /var/cache/apt/archives/* /var/www/html/* /usr/local/src/* /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && apt-get purge -y exim4 exim4-base exim4-config exim4-daemon-light \
    && apt-get autoremove -y \
    && rm -rf /usr/local/etc/php-fpm.d/* && mkdir -p /var/www/pic \
    && echo Europe/Kiev >/etc/timezone &&  dpkg-reconfigure -f noninteractive tzdata

# WORKDIR
WORKDIR /var/www/pic

# run service supervisord 
COPY conf.d/services  /etc/supervisor/conf.d/
#nginx
COPY nginx/      /etc/nginx/

#php
COPY php-fpm/php-fpm.conf /usr/local/etc/php-fpm.conf
COPY php-fpm/www.conf     /usr/local/etc/php-fpm.d/www.conf
COPY php-fpm/php.ini      /usr/local/etc/php/php.ini
RUN  mkdir /var/log/php
#rsyslog
COPY rsyslog.d/rsyslog.conf   /etc/rsyslog.conf
COPY rsyslog.d/02-phtsio.conf /etc/rsyslog.d/

# Install New Relic daemon

RUN wget -O - https://download.newrelic.com/548C16BF.gpg | apt-key add - \
    && echo "deb http://apt.newrelic.com/debian/ newrelic non-free" > /etc/apt/sources.list.d/newrelic.list \
    && apt-get update && apt-get -yq install newrelic-php5 newrelic-php5-common newrelic-daemon \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && unlink /etc/localtime \
    && ln -s /usr/share/zoneinfo/Europe/Kiev /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && useradd -m -s /bin/bash -u 1033 wdata && mkdir -p /var/www/app

# EXPOSE
EXPOSE 80 443

# ENTRYPOINT
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT [""]
CMD ["/entrypoint.sh"]
