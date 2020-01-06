FROM ubuntu

MAINTAINER John Wooten/CONSULTED <jwooten@cloudconsulted.com>

ENV DEBIAN_FRONTEND noninteractive
ENV JOOMLA_VERSION 3.4.1

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    mysql-server \
    apache2 \
    php5 \
    php5-imap \
    php5-mcrypt \
    php5-gd \
    php5-curl \
    php5-apcu \
    php5-mysqlnd \
    supervisor

# Download joomla and put it default apache web root
ADD https://github.com/joomla/joomla-cms/releases/download/$JOOMLA_VERSION/Joomla_$JOOMLA_VERSION-Stable-Full_Package.tar.gz /tmp/joomla/
RUN tar -zxvf /tmp/joomla/Joomla_$JOOMLA_VERSION-Stable-Full_Package.tar.gz -C /tmp/joomla/
RUN rm -rf /var/www/html/*
RUN cp -r /tmp/joomla/* /var/www/html/

# Put default htaccess in place
RUN mv /var/www/html/htaccess.txt /var/www/html/.htaccess

RUN chown -R www-data:www-data /var/www

# Expose HTTP and MySQL
EXPOSE 80 3306

# Use supervisord to start apache / mysql
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord", "-n"]
