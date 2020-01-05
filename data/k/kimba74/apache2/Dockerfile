FROM debian:8.0
MAINTAINER Steffen Krause <steffen.krause@soabridge.com>

# Update APT cache, install Apache2, and clean up
RUN apt-get update \
 && apt-get -y install apache2 curl \
 && apt-get clean

# Setting Apache2 runtime environment variables
ENV APACHE_RUN_USER=www-data \
    APACHE_RUN_GROUP=www-data \
    APACHE_LOG_DIR=/var/log/apache2

# Setting the fully qualified domain name for Apache2
RUN echo "ServerName `hostname`" > /etc/apache2/conf-available/fully-qualified-domain-name.conf \
 && a2enconf fully-qualified-domain-name

# For convenience of packaging new web sites set workdir to /var/www
WORKDIR /var/www

# Exposing port 80
EXPOSE 80

# Setting enty point for this container
ENTRYPOINT ["/usr/sbin/apache2ctl"]

# Setting default command
CMD ["-D", "FOREGROUND"]


