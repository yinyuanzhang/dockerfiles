FROM alpine:3.6
MAINTAINER Simon Ball <open-source@simonball.me>

USER root

RUN apk --update add \
  php7 \
  php7-apcu \
  php7-bcmath \
  php7-dom \
  php7-ctype \
  php7-curl \
  php7-fileinfo \
  php7-gd \
  php7-gettext \
  php7-iconv \
  php7-intl \
  php7-json \
  php7-ldap \
  php7-mbstring \
  php7-mcrypt \
  php7-opcache \
  php7-openssl \
  php7-pdo \
  php7-phar \
  php7-posix \
  php7-simplexml \
  php7-session \
  php7-soap \
  php7-tokenizer \
  php7-xml \
  php7-xmlreader \
  php7-xmlwriter \
  php7-zip \
  php7-zlib \
  php7-pcntl \
  php7-sockets \
  php7-sysvsem \
  autoconf \
  bash \
  ca-certificates \
  curl \
  git \
  libsasl \
  openssh \
  && ssh-keygen -A

COPY tools/phing /usr/local/bin/phing
COPY php.ini /etc/php7/php.ini

# Add timezone
RUN rm /etc/localtime && \
    ln -s /usr/share/zoneinfo/UTC /etc/localtime && \
"date"

# Grab the latest Composer install
RUN curl -sS https://getcomposer.org/installer | \
  php -- --install-dir=/usr/local/bin --filename=composer && \
  composer --version
# Install composer plugin for parallel downloads
RUN composer global require hirak/prestissimo

# Cleanup
RUN rm -rf /var/cache/apk/* \
    && find / -type f -iname \*.apk-new -delete \
&& rm -rf /var/cache/apk/*

WORKDIR /srv

CMD ["/bin/bash"]
