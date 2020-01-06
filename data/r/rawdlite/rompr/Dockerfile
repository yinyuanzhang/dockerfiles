FROM ubuntu:trusty
MAINTAINER rawdlite@gmail.com

# Install packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
  apt-get -y install supervisor curl apache2 libapache2-mod-php5 mysql-server php5-mysql php5-curl unzip imagemagick php5-json pwgen php-apc php5-mcrypt && \
  echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Add image configuration and scripts
ADD start-apache2.sh /start-apache2.sh
ADD start-mysqld.sh /start-mysqld.sh
ADD run.sh /run.sh
RUN chmod 755 /*.sh
ADD my.cnf /etc/mysql/conf.d/my.cnf
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf
ADD supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf

# Remove pre-installed database
RUN rm -rf /var/lib/mysql/*
# Add MySQL utils
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh
ADD init_rompr_db.sh /init_rompr_db.sh
RUN chmod 755 /*.sh
# config to enable .htaccess
ADD apache_default /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite
RUN a2enmod expires
RUN a2enmod headers
RUN a2enmod deflate
RUN a2enmod php5
# Configure /app folder with sample app
RUN curl -L -o rompr.zip http://sourceforge.net/projects/rompr/files/latest/download?source=files
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html
RUN unzip -d /app rompr.zip
RUN chown -R www-data /app/rompr/prefs
RUN chown -R www-data /app/rompr/albumart
#Environment variables to configure php
ENV PHP_UPLOAD_MAX_FILESIZE 32M
ENV PHP_POST_MAX_SIZE 32M
ENV PHP_REGISTER_GLOBALS Off
ENV PHP_MEMORY_LIMIT 256M
ENV PHP_MAX_EXECUTION_TIME  300
RUN echo "<?php phpinfo(); ?>" > /app/rompr/phpinfo.php
# Add volumes for MySQL 
VOLUME  ["/etc/mysql", "/var/lib/mysql" ]

EXPOSE 80 3306
CMD ["/run.sh"]
