FROM phusion/baseimage:0.9.15
MAINTAINER Patairmax

# Set correct environment variables.
ENV HOME /home

# Add user 1000
RUN adduser --ingroup www-data svcorp1000
# Add user 1001 as user on Google Compute
RUN adduser --ingroup www-data svcorp

# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ...put your own build instructions here...
#Install git for composer installation in some cases and php5-sqlite to have a PDO driver, else Symfony check bug :(
RUN apt-get update && apt-get -y install apache2 apache2-utils libapache2-mod-php5 php5 php5-cli php5-json php5-intl php5-apcu php5-gd php5-curl php5-mcrypt php5-mongo git php5-sqlite php-apc
RUN mkdir /etc/service/apache2
ADD apache2.sh /etc/service/apache2/run
COPY apache2.conf /etc/apache2/sites-available/000-default.conf
COPY php/apache2/php.ini /etc/php5/apache2/php.ini
COPY php/cli/php.ini /etc/php5/cli/php.ini

#COPY etc/fstab /etc/fstab

RUN mkdir /var/cache/symfony
RUN chown svcorp /var/cache/symfony
#RUN chown www-data /var/cache/symfony
RUN chgrp www-data /var/cache/symfony
RUN chmod 775 /var/cache/symfony
RUN mkdir /var/log/symfony
#RUN chown svcorp /var/log/symfony
RUN chown www-data /var/log/symfony
RUN chgrp www-data /var/log/symfony
RUN chmod 775 /var/log/symfony

#ENV APACHE_RUN_USER root
ENV APACHE_RUN_USER svcorp
##ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV LANG C


VOLUME ["/var/www/symfony"] 
WORKDIR /var/www/symfony

# Enable php5-mcrypt (not enabled by default)
RUN php5enmod mcrypt

# Turn on some crucial apache mods
RUN a2enmod rewrite headers

EXPOSE 80

#CMD ["/usr/sbin/a2ensite", "apache2"]
#CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
#CMD ["apache2", "-DFOREGROUND"]

ADD home/.bash_aliases /home/svcorp/.bash_aliases
RUN chown svcorp /home/svcorp/.bash_aliases
RUN chgrp www-data /home/svcorp/.bash_aliases
RUN chmod 755 /home/svcorp/.bash_aliases

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


