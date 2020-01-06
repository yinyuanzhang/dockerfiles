############################################################
# Dockerfile to build Apache2 and PHP Installed Containers
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu:12.04

# File Author / Maintainer
MAINTAINER Kaushal Kishore <kaushal.rahuljaiswal@gmail.com>

# Update the repository
RUN apt-get update

# Download and Install Apache2
RUN apt-get install -y apache2

# Setting up the Enviroment Variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

# Download and Install PHP
RUN apt-get install -y php5 libapache2-mod-php5 php5-mysql php5-gd php-pear php-apc php5-curl curl lynx-cur

# Enable apache mods.
RUN a2enmod php5
RUN a2enmod rewrite

# Set the Volume
VOLUME /var/www

# Set the port
EXPOSE 80

# Set the entry point for the apache
ENTRYPOINT ["/usr/sbin/apache2"]
CMD ["-D", "FOREGROUND"]
