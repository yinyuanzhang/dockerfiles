#
# PureFTPD build stage
# Inspired by stilliard's docker-pure-ftpd build steps:
# https://github.com/stilliard/docker-pure-ftpd
#
FROM ubuntu:bionic as pureftpd

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -q -y --no-install-recommends \
        build-essential curl ca-certificates tar libssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /tmp/pure-ftpd/ \
	&& cd /tmp/pure-ftpd/ \
    && curl -fsSL https://download.pureftpd.org/pub/pure-ftpd/releases/pure-ftpd-1.0.49.tar.gz > pure-ftpd.tar.gz \
    && tar -xzvf pure-ftpd.tar.gz \
    && cd pure-ftpd-* \
    && ./configure --with-tls --with-extauth --with-virtualchroot --with-uploadscript --without-inetd --without-sendfile \
    && sed -i '/CAP_SYS_NICE,/d; /CAP_DAC_READ_SEARCH/d; s/CAP_SYS_CHROOT,/CAP_SYS_CHROOT/;' src/caps_p.h \
    && make install-strip \
    && rm -rf /tmp/pure-ftpd

#
# Main build stage
#
FROM phusion/baseimage:0.11

# Set time zone
ENV TZ="UTC"
RUN echo $TZ > /etc/timezone

# Install essential packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -q -y --no-install-recommends apt-transport-https \
        ca-certificates curl wget tar software-properties-common sudo zip unzip git rsync tzdata \
        tmpreaper mariadb-client \
        nginx nginx-common nginx-extras \
        openbsd-inetd lsb-base libc6 libcap2 libpam0g libssl1.1 openssl \
    && wget -qO- https://repos.influxdata.com/influxdb.key | apt-key add - \
    && echo "deb https://repos.influxdata.com/ubuntu bionic stable" | tee /etc/apt/sources.list.d/influxdb.list \
    && add-apt-repository -y ppa:certbot/certbot \
    && add-apt-repository -y ppa:ondrej/php \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -q -y --no-install-recommends \
        certbot influxdb \
        php7.4-fpm php7.4-cli php7.4-gd \
        php7.4-curl php7.4-xml php7.4-zip php7.4-bcmath \
        php7.4-mysqlnd php7.4-mbstring php7.4-intl php7.4-redis \
    && rm -rf /var/lib/apt/lists/*

# Create azuracast user.
RUN adduser --home /var/azuracast --disabled-password --gecos "" azuracast \
    && usermod -aG docker_env azuracast \
    && usermod -aG www-data azuracast \
    && mkdir -p /var/azuracast/www /var/azuracast/backups /var/azuracast/www_tmp /var/azuracast/geoip \
    && chown -R azuracast:azuracast /var/azuracast \
    && chmod -R 777 /var/azuracast/www_tmp \
    && echo 'azuracast ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

# Install nginx and configuration
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./nginx/azuracast.conf /etc/nginx/conf.d/azuracast.conf

# Create nginx and FTP temp dirs
RUN mkdir -p /tmp/azuracast_nginx_client /tmp/azuracast_fastcgi_temp /tmp/azuracast_ftp_directories \
    && touch /tmp/azuracast_nginx_client/.tmpreaper \
    && touch /tmp/azuracast_fastcgi_temp/.tmpreaper \
    && touch /tmp/azuracast_ftp_directories/.tmpreaper \
    && chmod -R 777 /tmp/azuracast_*

# Generate the dhparam.pem file (takes a long time)
RUN openssl dhparam -dsaparam -out /etc/nginx/dhparam.pem 4096

# Set certbot permissions
RUN mkdir -p /var/www/letsencrypt /var/lib/letsencrypt /etc/letsencrypt /var/log/letsencrypt \
    && chown -R azuracast:azuracast /var/www/letsencrypt /var/lib/letsencrypt /etc/letsencrypt /var/log/letsencrypt

# Install pure-ftpd from build container
COPY --from=pureftpd /usr/local/sbin/pure-* /usr/local/sbin/

# Copy pure-ftpd config
COPY ./pure-ftpd/pure-ftpd.conf /etc/pure-ftpd.conf

# Install PHP 7.2
RUN mkdir -p /run/php
RUN touch /run/php/php7.4-fpm.pid

COPY ./php/php.ini.tmpl /etc/php/7.4/fpm/05-azuracast.ini.tmpl
COPY ./php/www.conf.tmpl /etc/php/7.4/fpm/www.conf.tmpl

# Install Dockerize
ENV DOCKERIZE_VERSION="v0.6.1"
RUN wget --quiet https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

# AzuraCast installer and update commands
COPY scripts/ /usr/local/bin
RUN chmod -R a+x /usr/local/bin

# Set up first-run scripts and runit services
COPY ./startup_scripts/ /etc/my_init.d/
COPY ./runit/ /etc/service/

RUN chmod +x /etc/service/*/run \
    && chmod +x /etc/my_init.d/*

# Copy crontab
COPY ./cron/ /etc/cron.d/

RUN chmod -R 600 /etc/cron.d/*

#
# START Operations as `azuracast` user
#
USER azuracast

# Add global Composer deps
RUN composer create-project azuracast/azuracast /var/azuracast/new ^0.9.8 --no-dev \
    && mv /var/azuracast/new/vendor /var/azuracast/www \
    && rm -rf /var/azuracast/new

# Alert AzuraCast that it's running in Docker mode
RUN touch /var/azuracast/.docker

# SSL self-signed cert generation
RUN openssl req -new -nodes -x509 -subj "/C=US/ST=Texas/L=Austin/O=IT/CN=localhost" \
    -days 365 -extensions v3_ca \
    -keyout /etc/letsencrypt/selfsigned.key \
	-out /etc/letsencrypt/selfsigned.crt

RUN ln -s /etc/letsencrypt/selfsigned.key /etc/letsencrypt/ssl.key \
    && ln -s /etc/letsencrypt/selfsigned.crt /etc/letsencrypt/ssl.crt

# Clone repo and set up AzuraCast repo
WORKDIR /var/azuracast/www
VOLUME ["/var/azuracast/www", "/var/azuracast/backups", "/etc/letsencrypt"]

#
# END Operations as `azuracast` user
#
USER root

EXPOSE 80 443

# Nginx Proxy environment variables.
ENV VIRTUAL_HOST="azuracast.local" \
    HTTPS_METHOD="noredirect"

# Sensible default environment variables.
ENV APPLICATION_ENV="production" \
    FTP_PASV_IP="localhost" \
    MYSQL_HOST="mariadb" \
    MYSQL_PORT=3306 \
    MYSQL_USER="azuracast" \
    MYSQL_PASSWORD="azur4c457" \
    MYSQL_DATABASE="azuracast" \ 
    PREFER_RELEASE_BUILDS="false" \
    COMPOSER_PLUGIN_MODE="false" \
    ADDITIONAL_MEDIA_SYNC_WORKER_COUNT=0

# Entrypoint and default command
ENTRYPOINT ["dockerize",\
    "-wait","tcp://mariadb:3306",\
    "-wait","tcp://influxdb:8086",\
    "-timeout","40s"]
CMD ["/sbin/my_init"]
