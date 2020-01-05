FROM phusion/baseimage:0.11

# Set time zone
ENV TZ="UTC"
RUN echo $TZ > /etc/timezone

# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.
RUN sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d

# Install essential packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -q -y --no-install-recommends apt-transport-https \
        ca-certificates curl wget tar software-properties-common sudo zip unzip git tzdata \
        nginx nginx-common nginx-extras \
        php7.2-fpm php7.2-cli php7.2-gd \
        php7.2-curl php7.2-xml php7.2-zip php7.2-mysqlnd php7.2-mbstring php7.2-intl php7.2-redis

# Create azuracast user.
RUN adduser --home /var/azuracast --disabled-password --gecos "" azuracast \
    && usermod -aG docker_env azuracast \
    && mkdir -p /var/azuracast/www \
    && mkdir -p /var/azuracast/www_tmp \
    && mkdir -p /var/azuracast/geoip \
    && mkdir -p /etc/letsencrypt \
    && chown -R azuracast:azuracast /var/azuracast \
    && chown -R azuracast:azuracast /etc/letsencrypt \
    && chmod -R 777 /var/azuracast/www_tmp \
    && echo 'azuracast ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

# Install PHP 7.2
RUN mkdir -p /run/php
RUN touch /run/php/php7.2-fpm.pid

COPY ./php/php.ini /etc/php/7.2/fpm/conf.d/05-azuracast.ini
COPY ./php/php.ini /etc/php/7.2/cli/conf.d/05-azuracast.ini
COPY ./php/phpfpmpool.conf /etc/php/7.2/fpm/pool.d/www.conf

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

# AzuraCast installer and update commands
COPY scripts/ /usr/local/bin
RUN chmod -R a+x /usr/local/bin

# Install MaxMind GeoIP Lite
RUN wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz \
    && tar -C /var/azuracast/geoip -xzvf GeoLite2-City.tar.gz --strip-components 1 \
    && rm GeoLite2-City.tar.gz \
    && chown -R azuracast:azuracast /var/azuracast/geoip

# Install Dockerize
ENV DOCKERIZE_VERSION="v0.6.1"
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Install nginx and configuration
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./nginx/azuracast.conf /etc/nginx/conf.d/azuracast.conf

# Install LetsEncrypt's certbot
RUN add-apt-repository universe \
    && add-apt-repository ppa:certbot/certbot \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -q -y --no-install-recommends certbot 

# Generate the dhparam.pem file (takes a long time)
RUN openssl dhparam -dsaparam -out /etc/nginx/dhparam.pem 4096

# Set up runit services
COPY ./runit/ /etc/service/

RUN chmod +x /etc/service/*/run

# Copy crontab
COPY ./cron/ /etc/cron.d/

#
# START Operations as `azuracast` user
#
USER azuracast

# Alert AzuraCast that it's running in Docker mode
RUN touch /var/azuracast/.docker

# SSL self-signed cert generation
RUN openssl req -new -nodes -x509 -subj "/C=US/ST=Texas/L=Austin/O=IT/CN=localhost" \
    -days 365 -extensions v3_ca \
    -keyout /etc/letsencrypt/selfsigned.key \
	-out /etc/letsencrypt/selfsigned.crt

RUN ln -s /etc/letsencrypt/selfsigned.key /etc/letsencrypt/ssl.key \
    && ln -s /etc/letsencrypt/selfsigned.crt /etc/letsencrypt/ssl.crt

VOLUME /etc/letsencrypt

# Clone repo and set up AzuraCast repo
WORKDIR /var/azuracast/www

RUN git clone --shallow-since=2018-11-15 https://github.com/AzuraCast/AzuraCast.git . \
    && composer install -o --no-dev

VOLUME /var/azuracast/www

#
# END Operations as `azuracast` user
#
USER root

# Sensible default environment variables.
ENV APPLICATION_ENV="production" \
    MYSQL_HOST="mariadb" \
    MYSQL_PORT=3306 \
    MYSQL_USER="azuracast" \
    MYSQL_PASSWORD="azur4c457" \
    MYSQL_DATABASE="azuracast"

# Entrypoint and default command
ENTRYPOINT ["dockerize","-wait","tcp://mariadb:3306","-wait","tcp://influxdb:8086","-timeout","20s"]
CMD ["/sbin/my_init"]