FROM ubuntu:16.04

RUN apt-get update
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y php php-pear php-fpm php-dev php-zip php-curl php-xmlrpc php-gd php-mysql php-mbstring php-xml libapache2-mod-php iptables
RUN apt-get install -y apache2
RUN adduser mememastero
RUN mkdir /var/www/html/memes && chown -R mememastero. /var/www/html/memes
ADD /configs/001-default.conf /etc/apache2/sites-available
RUN ln -s /etc/apache2/sites-available/001-default.conf /etc/apache2/sites-enabled && a2ensite 001-default.conf && a2dissite 000-default.conf
RUN systemctl enable apache2
CMD service apache2 start
EXPOSE 21 22 80 443 8080
