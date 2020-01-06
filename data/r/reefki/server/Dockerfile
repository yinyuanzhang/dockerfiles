# Pull base image
FROM alpine:latest

# Add metadata
LABEL maintainer "Rifki Aria Gumelar <rifki@rifki.net>"

# Set timezone
ENV TIMEZONE UTC
RUN apk add --no-cache tzdata \
    && cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \
    && echo ${TIMEZONE} > /etc/timezone

# Install softwares
RUN apk add --no-cache \
    beanstalkd \
    busybox-suid \
    caddy \
    composer \
    curl \
    git \
    libmemcached \
    nano \
    npm \
    php7 \
    php7-bcmath \
    php7-curl \
    php7-ctype \
    php7-dom \
    php7-exif \
    php7-fileinfo \
    php7-fpm \
    php7-ftp \
    php7-gd \
    php7-iconv \
    php7-json \
    php7-mbstring \
    php7-mysqli \
    php7-openssl \
    php7-pdo \
    php7-pdo_mysql \
    php7-pdo_pgsql \
    php7-pdo_sqlite \
    php7-pecl-imagick \
    php7-pecl-mcrypt \
    php7-pecl-memcached \
    # php7-pecl-mongodb \
    php7-pecl-redis \
    php7-pecl-ssh2 \
    php7-simplexml \
    php7-sodium \
    php7-sockets \
    php7-sqlite3 \
    php7-tokenizer \
    php7-xml \
    php7-xmlreader \
    php7-zip \
    supervisor \
    sqlite \
    zip

# Copy entrypoint file.
COPY ./start.sh /bin
RUN chmod 777 /bin/start.sh

# Copy Supervisor config file.
COPY ./supervisord.conf /etc/supervisord.conf

# Copy Caddy server config file.
COPY ./Caddyfile /etc/caddy/Caddyfile

# Set entrypoint
ENTRYPOINT [ "start.sh" ]

# Run command
CMD [ "supervisord", "-n", "-c", "/etc/supervisord.conf" ]

# Expose ports
EXPOSE 80 443 9000 11300
