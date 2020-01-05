FROM debian:jessie
MAINTAINER Ivan Alvarez <ivan.alvarez@ext.mpsa.com>

VOLUME ["/var/www"]

RUN apt-get update && \
    apt-get install -y \
      locales \
      apache2 \
      php5 \
      php5-cli \
      libapache2-mod-php5 \
      php5-gd \
      php5-json \
      php5-ldap \
      php5-mysql \
      php5-pgsql \
      php5-mcrypt \
      php5-intl
      

COPY apache_default /etc/apache2/sites-available/000-default.conf
COPY run.sh /usr/local/bin/run.sh
RUN chmod +x /usr/local/bin/run.sh
RUN a2enmod rewrite
RUN chown -R www-data:www-data /var/www/

EXPOSE 80
CMD ["/usr/local/bin/run.sh"]
