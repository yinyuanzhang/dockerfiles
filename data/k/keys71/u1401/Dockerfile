FROM ubuntu:14.04
MAINTAINER Robert Schwandner <rs@rob24.de>

ENV DEBIAN_FRONTEND noninteractive
ENV INITRD No

RUN apt-get update

# Configure repos
RUN apt-get install -y vim curl wget build-essential python-software-properties

RUN apt-get install -y --force-yes php5-cli php5-fpm php5-mysql php5-pgsql php5-sqlite php5-curl php5-gd php5-mcrypt php5-intl php5-imap php5-tidy

RUN sed -i "s/;date.timezone =.*/date.timezone = Europe\/Berlin/" /etc/php5/fpm/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = Europe\/Berlin/" /etc/php5/cli/php.ini

RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini

#RUN echo "mysql-server mysql-server/root_password password" | debconf-set-selections && \
#    echo "mysql-server mysql-server/root_password_again password" | debconf-set-selections

RUN  apt-get install -y mysql-server

RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf    
RUN sed -i 's/^key_buffer\s*=/key_buffer_size =/' /etc/mysql/my.cnf  
ADD set-mysql-password.sh /tmp/set-mysql-password.sh
RUN /bin/sh /tmp/set-mysql-password.sh  
    

RUN apt-get -qqy install nginx
ADD nginx_default.conf /etc/nginx/sites-available/default
ADD index.html /var/www/index.html
ADD index.php /var/www/index.php


# Supervisord
RUN apt-get -y install python-setuptools
RUN easy_install supervisor
ADD supervisord.conf /etc/supervisord.conf

# Expose ports.
EXPOSE 80 3306

CMD ["/usr/local/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]