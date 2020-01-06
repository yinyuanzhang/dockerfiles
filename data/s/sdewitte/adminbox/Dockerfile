FROM ubuntu:latest
ADD start.sh /start.sh
RUN chmod +x /start.sh
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install phpmyadmin apache2
RUN cd /etc/apache2/conf-available && ln -s /etc/phpmyadmin/apache.conf phpmyadmin.conf && a2enconf phpmyadmin.conf
RUN php5enmod mcrypt
VOLUME ["/etc/apache2/", "/etc/phpmyadmin/", "/var/www/", "/var/log/apache2/"]
ENTRYPOINT ["/start.sh"]
