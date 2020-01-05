FROM hitwe/base7:latest
MAINTAINER Marko <sergey.semenyuk@gen.tech>

############## NEWRELIC 
# Setup environment variables for initializing New Relic

ENV NR_INSTALL_SILENT 1
ENV NR_INSTALL_KEY e78318736324bb6aaeefc03ef325e825e23d5b3b
ENV NR_APP_NAME ""
ENV NEWRELIC_VERSION 6.8.0.177

# Install New Relic daemon

RUN wget -O - https://download.newrelic.com/548C16BF.gpg | apt-key add - \
    && echo "deb http://apt.newrelic.com/debian/ newrelic non-free" > /etc/apt/sources.list.d/newrelic.list \
    && apt-get update && apt-get -yq install newrelic-php5 newrelic-php5-common newrelic-daemon \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && unlink /etc/localtime \
    && ln -s /usr/share/zoneinfo/Europe/Kiev /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && useradd -m -s /bin/bash -u 1033 wdata && mkdir -p /var/www/app

ENV POOL_ENV     www
ENV MEMCACHED_IP 10.53.129.180
ENV RSYSLOG_IP   10.53.131.196

COPY php-fpm.conf /usr/local/etc/php-fpm.conf
COPY php-fpm.d /usr/local/etc/php-fpm.d
COPY php/php.ini /usr/local/etc/php/php.ini
COPY php/docker-php-ext-opcache.ini /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini

# Добавления конфигов
COPY nginx/nginx.conf  /etc/nginx/nginx.conf 
COPY nginx/clean.conf /etc/nginx/conf.d/default.conf 

### Установка конфига rsyslog
COPY rsyslog.conf  /etc/rsyslog.conf 
COPY rsyslog.d/03-servers-backends.conf  /etc/rsyslog.d/03-servers-backends.conf

#Рабочая папка 
WORKDIR /var/www/app
COPY conf.d/all /etc/supervisor/conf.d/all

# Replace base7 supervisord.conf
COPY supervisord.conf /etc/supervisor/

# Supervisor email notification script
COPY scripts/crashmail.py /etc/supervisor/

# New Relic isights script
COPY scripts/newrelic-insights.sh /usr/local/bin/

#copy opcache app
COPY opcache /var/www/opcache

COPY entrypoint.sh /entrypoint.sh
#RUN  chmod +x /entrypoint.sh
ENTRYPOINT [""]
CMD ["/entrypoint.sh"]
