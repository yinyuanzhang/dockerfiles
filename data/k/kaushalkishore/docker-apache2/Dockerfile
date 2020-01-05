############################################################
# Dockerfile to build Apache2 Installed Containers
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

# Set the Volume
VOLUME /var/www

# Set the port
EXPOSE 80

# Set the entry point for the apache
ENTRYPOINT ["/usr/sbin/apache2"]
CMD ["-D", "FOREGROUND"]
