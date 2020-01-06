FROM ubuntu:bionic

RUN set -x \
	&& apt-get update -y  \
        && apt-get upgrade -y \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
                   wget nginx \
        \
	&& apt-get install --no-install-recommends --no-install-suggests -y software-properties-common \
        && add-apt-repository ppa:ondrej/php \
        \
        && apt-get update --no-install-recommends --no-install-suggests -y \
        && apt-get install --no-install-recommends --no-install-suggests -y php7.3-fpm php7.3-common php7.3-mbstring \
                       php7.3-xmlrpc php7.3-soap php7.3-gd php7.3-xml \
                       php7.3-intl php7.3-mysql php7.3-cli \
                       php7.3-ldap php7.3-zip php7.3-curl 

COPY    etc/php/7.3/fpm/php.ini /etc/php/7.3/fpm/
COPY    etc/php/7.3/fpm/php-fpm.conf /etc/php/7.3/fpm/
COPY    etc/php/7.3/fpm/pool.d/www.conf /etc/php/7.3/fpm/pool.d/

# Define Joomla version and expected SHA1 signature
ENV JOOMLA_VERSION 3.9.3
ENV JOOMLA_SHA1 ff403cced4f9559f286ad6c026008cc1b9543b72

RUN set -x \
        && cd /tmp \
        && wget https://github.com/joomla/joomla-cms/releases/download/${JOOMLA_VERSION}/Joomla_${JOOMLA_VERSION}-Stable-Full_Package.zip \
        && echo "$JOOMLA_SHA1 Joomla_${JOOMLA_VERSION}-Stable-Full_Package.zip" | sha1sum -c - \
	&& apt-get install --no-install-recommends --no-install-suggests -y unzip \
#	&& unzip Joomla*.zip \
	&& mkdir -p /var/www/html/joomla \
	&& unzip Joomla_${JOOMLA_VERSION}-Stable-Full_Package.zip -d /var/www/html/joomla \
        \
        && chown -R www-data:www-data /var/www/html/joomla/ \
        && chmod -R 755 /var/www/html/joomla/    

COPY    etc/nginx/sites-available/default /etc/nginx/sites-available/       

VOLUME  /var/www/html

RUN     ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

RUN     apt-get install -y supervisor
RUN     mkdir -p /var/log/supervisor
RUN     mkdir -p /etc/supervisor/conf.d

COPY    etc/supervisor/supervisor.conf /etc/supervisor/supervisor.conf

EXPOSE 80
EXPOSE 443

STOPSIGNAL SIGTERM

COPY docker-entrypoint.sh /entrypoint.sh
COPY makedb.php /makedb.php

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["supervisord", "-n", "-c", "/etc/supervisor/supervisor.conf"]

