FROM ubuntu:xenial

# Install apache
RUN echo "deb http://ppa.launchpad.net/ondrej/apache2/ubuntu xenial main" > /etc/apt/sources.list.d/ondrej.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C
RUN apt-get -qq update && apt-get install -yqq apache2
RUN service apache2 stop

# Activating configuration
RUN a2enmod http2 headers proxy_fcgi rewrite ssl alias autoindex vhost_alias expires
RUN cd /etc/apache2/conf-enabled; a2disconf *
RUN cd /etc/apache2/sites-enabled; a2dissite *
COPY ./conf/apache2.conf /etc/apache2/apache2.conf
COPY ./conf/conf-available /etc/apache2/conf-available
COPY ./conf/sites-available /etc/apache2/sites-available
COPY ./conf/certificates /etc/apache2/certificates
RUN cd /etc/apache2/sites-enabled; a2ensite 000-default
RUN cd /etc/apache2/conf-enabled; a2enconf charset php7.3-fpm security

WORKDIR /wwwroot
CMD apachectl -D FOREGROUND
