FROM debian:9.4
MAINTAINER inox42

# update
RUN apt-get update; apt-get upgrade -y
RUN apt-get install -y unzip wget

# install nginx
RUN apt-get install -y nginx
RUN ip addr show eth0 | grep inet | awk '{ print $2; }' | sed 's/\/.*$//'
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# install php5.0-fpm
RUN echo "deb http://mirrors.digitalocean.com/debian jessie main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.digitalocean.com/debian jessie main contrib non-free" >> /etc/apt/sources.list

RUN echo "deb http://security.debian.org/ jessie/updates main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb-src http://security.debian.org/ jessie/updates main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb http://mirrors.digitalocean.com/debian jessie-updates main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.digitalocean.com/debian jessie-updates main contrib non-free" >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y php5-fpm php5-mysql php5-ldap php5-imap

# install grr
ENV GRR_VERSION="3-4-0-rc2"
RUN wget "https://site.devome.com/fr/grr/telechargement/category/3-versions-patch?download=23:grr-"$GRR_VERSION -O /tmp/GRR-$GRR_VERSION.zip
RUN cd /tmp;unzip /tmp/GRR-$GRR_VERSION.zip
RUN rm -f /tmp/GRR-$GRR_VERSION.zip

# configure GRR & nginx
RUN mv /tmp/GRR* /var/www/GRR
COPY grr/site-grr /etc/nginx/sites-enabled/default
COPY grr/startup.sh /startup.sh
RUN chown -R www-data /var/www/GRR
RUN chmod 644 /var/www/GRR/include/connect.inc.php

ENV MYSQL_HOST="db"
ENV MYSQL_DATABASE="grr"
ENV MYSQL_USER="grr"
ENV MYSQL_PASSWORD="grr"
ENV MYSQL_PREFIX="grr"
ENV MYSQL_PORT=""

# expose ports
EXPOSE 80

# Entrypoint
CMD ["/startup.sh"]
