FROM ubuntu:14.04
MAINTAINER Darren Worrall, darren@iweb.co.uk

RUN apt-get update
RUN apt-get install -qy apache2 php5-fpm supervisor libapache2-mod-rpaf
# Common PHP modules
RUN apt-get install -qy php5-cgi php5-mysql php5-gd php5-curl php5-cli php5-xsl php5-memcache php5-mcrypt php5-redis

RUN a2enmod expires rewrite headers proxy_fcgi
RUN rm -r /var/www/html/*

RUN mkdir -p /var/log/supervisor
# Default timezone
RUN sed -i 's/;date\.timezone.*/date.timezone = Europe\/London/g' /etc/php5/fpm/php.ini
RUN php5enmod mcrypt

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD apache_extra.conf /etc/apache2/conf-enabled/apache_extra.conf
ADD www.conf /etc/php5/fpm/pool.d/www.conf

EXPOSE 80
CMD ["/usr/bin/supervisord"]
