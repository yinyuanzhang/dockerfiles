FROM debian:jessie

RUN  apt-get update  && apt-get install -y apache2 php5 libapache2-mod-php5 php5-mcrypt php5-gd && apt-get clean -y && a2enmod php5

COPY index.html index.php /var/www/html/

ENTRYPOINT ["/usr/sbin/apachectl", "-d /etc/apache2 -f apache2.conf -DFOREGROUND"]

EXPOSE 80
