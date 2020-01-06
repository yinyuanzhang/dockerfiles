FROM library/ubuntu:16.04
LABEL maintainer="Rasmus Dybro Larsen"

RUN apt-get -y update
RUN apt-get -y install libapache2-mod-php7.0 php7.0-cli php7.0-mysql php7.0-gd php7.0-snmp php-pear php7.0-curl snmp graphviz php7.0-mcrypt php7.0-json apache2 fping imagemagick whois mtr-tiny nmap python-mysqldb snmpd php-net-ipv4 php-net-ipv6 rrdtool git

# REMEMBER:
# In /etc/php/7.0/apache2/php.ini and /etc/php/7.0/cli/php.ini, ensure date.timezone is set to your preferred time zone. See http://php.net/manual/en/timezones.php for a list of supported timezones. Valid examples are: "America/New_York", "Australia/Brisbane", "Etc/UTC".

RUN a2enmod php7.0
RUN a2dismod mpm_event
RUN a2enmod mpm_prefork
RUN phpenmod mcrypt

RUN useradd librenms -d /opt/librenms -M -r
RUN usermod -a -G librenms www-data

RUN git clone https://github.com/librenms/librenms.git /opt/librenms

RUN mkdir /opt/librenms/rrd /opt/librenms/logs
RUN chmod 775 /opt/librenms/rrd

ADD config.php /opt/librenms/config.php
ADD librenms.conf /etc/apache2/sites-available/librenms.conf

RUN a2ensite librenms.conf
RUN a2enmod rewrite
RUN a2dissite 000-default
RUN service apache2 restart; exit

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_SERVERADMIN librenms@localhost
ENV APACHE_SERVERNAME localhost
ENV APACHE_SERVERALIAS librenms.localhost
ENV APACHE_DOCUMENTROOT /var/www

EXPOSE 80
VOLUME /opt/librenms

#CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]