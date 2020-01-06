FROM ubuntu:trusty
MAINTAINER Michael Holt

# Install packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
  apt-get -y install supervisor git apache2 libapache2-mod-php5 mysql-server php5-mysql pwgen php-apc \
  php5-mcrypt php5-mcrypt php5-gd php5-ldap php5-cli php-soap php5-json graphviz wget unzip && \
  echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Add image configuration and scripts
ADD start-apache2.sh /start-apache2.sh
ADD run.sh /run.sh
RUN chmod 755 /*.sh
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf

RUN php5enmod mcrypt ldap gd

RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html

# Add cron config and scripts
ADD supervisord-cron.conf /etc/supervisor/conf.d/supervisord-cron.conf
ADD start-cron.sh /start-cron.sh
ADD setup-itop-cron.sh /setup-itop-cron.sh

# Add update Russian translations script
ADD update-russian-translations.sh /update-russian-translations.sh

# Add Portal Announcement Extension install script
ADD install-portal-announcement.sh /install-portal-announcement.sh
ADD update-portal-announcement.sh /update-portal-announcement.sh

# Add iTop config-file rights management scripts
ADD make-itop-config-writable.sh /make-itop-config-writable.sh
ADD make-itop-config-read-only.sh /make-itop-config-read-only.sh

# Add Tookit installation script
ADD install-toolkit.sh /install-toolkit.sh

RUN chmod 755 /*.sh

# Get iTop 2.3.1
RUN mkdir -p /tmp/itop
RUN wget -O /tmp/itop/itop.zip https://sourceforge.net/projects/itop/files/itop/2.3.1/iTop-2.3.1-2832.zip
RUN unzip /tmp/itop/itop.zip -d /tmp/itop/

# Configure /app folder with iTop
RUN rm -fr /app
RUN mkdir -p /app && cp -r /tmp/itop/web/* /app && rm -rf /tmp/itop

# Get latest Russian translations
RUN /update-russian-translations.sh

RUN chown -R www-data:www-data /app

#Enviornment variables to configure php
ENV PHP_UPLOAD_MAX_FILESIZE 8M
ENV PHP_POST_MAX_SIZE 10M

EXPOSE 80
CMD ["/run.sh"]
