# Build static files container
FROM node:10.15.3 AS buildstatic

COPY . /app
WORKDIR /app

RUN npm install -y
RUN cd /app \
	&& npm run js-minify \
	&& npm run css-compile

FROM ubuntu:18.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 \
      libapache2-mod-php php-gd php-curl php-memcached curl python-setuptools \
	  python-pip php-sqlite3 php-xml  php-mbstring php-cli cron && \
	rm -rf /var/lib/apt/lists/* && \
	pip install supervisor

RUN a2enmod php7.2
RUN a2enmod rewrite
RUN cp /etc/apache2/mods-available/expires.load /etc/apache2/mods-enabled/

RUN sed -i 's/memory_limit\ =\ 128M/memory_limit\ =\ 2G/g' /etc/php/7.2/apache2/php.ini
RUN sed -i 's/\;date\.timezone\ =/date\.timezone\ =\ America\/Sao_Paulo/g' /etc/php/7.2/apache2/php.ini
RUN sed -i 's/display_errors\ =\ On/display_errors\ =\ Off/g' /etc/php/7.2/apache2/php.ini

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV CI_ENV production

ADD . /var/www/site/
COPY --from=buildstatic /app/static/ /var/www/site/static/
COPY docker/application-cron /etc/cron.d/application-cron

ADD docker/apache-config.conf /etc/apache2/sites-enabled/000-default.conf
ADD docker/foreground.sh /etc/apache2/foreground.sh
ADD docker/supervisord.conf /etc/supervisord.conf

RUN chmod -R 0777 /var/www/site/application/cache
RUN chmod 755 /etc/apache2/foreground.sh
RUN mkdir /var/log/supervisor/

RUN chmod 0644 /etc/cron.d/application-cron
RUN crontab /etc/cron.d/application-cron

RUN php /var/www/site/index.php cache_util update_database

WORKDIR /var/www/site
EXPOSE 80
CMD ["supervisord" , "-n", "-c", "/etc/supervisord.conf"]

