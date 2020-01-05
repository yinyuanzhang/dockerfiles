FROM debian:stretch-slim
MAINTAINER Diksy M. Firmansyah <diksy@unej.ac.id>

# update timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Jakarta /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata
# update OS
RUN sed -i s/deb.debian.org/mirror.unej.ac.id/g /etc/apt/sources.list
RUN apt-get update
RUN apt-get dist-upgrade -y
# install apache2 & php7
RUN apt-get install -y apache2 libapache2-mod-php php-mysql php-pgsql
RUN echo "ServerName 'localhost'" >> /etc/apache2/apache2.conf
RUN a2dismod mpm_event
RUN a2enmod mpm_prefork rewrite

VOLUME ["/var/www/", "/etc/apache2/sites-available/"]
EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
