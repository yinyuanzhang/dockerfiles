FROM driou/debian-base
MAINTAINER Adrien Bourroux <a.bourroux@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
# Updating Package List
RUN apt-get update

# Installing Nginx package
RUN apt-get install -y nginx 
 
# Installing PHP Packages
RUN apt-get install -y php5-fpm	
RUN apt-get install -y php5-curl php5-gd php5-intl php5-json php5-mcrypt php5-mysqlnd php5-readline

# Installing Mysql Packages
RUN echo "mysql-server mysql-server/root_password password toor" | debconf-set-selections && \
echo "mysql-server mysql-server/root_password_again password toor" | debconf-set-selections 
RUN apt-get install -y mysql-server

RUN apt-get install -y supervisor
RUN chown -R www-data. /usr/share/nginx/html/ && \
	chmod -R 755 /usr/share/nginx/html/

ADD supervisor/php5-fpm.conf /etc/supervisor/conf.d/php5-fpm.conf
ADD supervisor/nginx.conf /etc/supervisor/conf.d/nginx.conf
ADD supervisor/mysql.conf /etc/supervisor/conf.d/mysql.conf

WORKDIR /usr/share/nginx/html/

VOLUME /etc/nginx/sites-enabled/
VOLUME /etc/php5/fpm/
VOLUME /usr/share/nginx/html/

EXPOSE 80
CMD ["/usr/bin/supervisord", "--nodaemon", "-c", "/etc/supervisor/supervisord.conf"]

