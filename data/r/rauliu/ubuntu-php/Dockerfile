FROM rauliu/ubuntu-base
MAINTAINER Raul Liu "https://github.com/rauliu"

# Update sources
RUN apt-get update -y

# install http
RUN apt-get install -y apache2 vim bash-completion unzip
RUN mkdir -p /var/lock/apache2 /var/run/apache2

# install mysql
#RUN apt-get install -y mysql-client mysql-server

# install php
RUN apt-get install -y php5 php5-mysql php5-dev php5-gd php5-memcache php5-pspell php5-snmp snmp php5-xmlrpc libapache2-mod-php5 php5-cli

#Set up sendmail for PHP
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise universe" >> /etc/apt/sources.list
RUN apt-get -q -y update
RUN apt-get install -q -y msmtp ca-certificates

RUN touch /etc/msmtprc
RUN mkdir -p /var/log/msmtp
RUN chown www-data:adm /var/log/msmtp
RUN touch /etc/logrotate.d/msmtp
RUN rm /etc/logrotate.d/msmtp
RUN echo "/var/log/msmtp/*.log {\n rotate 12\n monthly\n compress\n missingok\n notifempty\n }" > /etc/logrotate.d/msmtp
RUN sed -i 's/;sendmail_path\s=.*/sendmail_path = \/usr\/bin\/msmtp -t/' /etc/php5/apache2/php.ini

ADD phpinfo.php /var/www/html/

ADD apache.conf /etc/supervisor/conf.d/

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

EXPOSE 22 80 443
