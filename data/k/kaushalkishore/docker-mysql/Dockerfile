############################################################
# Dockerfile to build MySQL-5.5 Installed Containers
# Based on Ubuntu 12.04
############################################################

# Set the base image to Ubuntu
FROM ubuntu:12.04

# File Author / Maintainer
MAINTAINER Kaushal Kishore <kaushal.rahuljaiswal@gmail.com>

# Set the enviroment variable
ENV DEBIAN_FRONTEND noninteractive

# Update the repository
RUN apt-get update

# Download and Installing MySQL Server-5.5
RUN apt-get -yq install mysql-server-5.5
RUN rm -rf /var/lib/apt/lists/*

# Remove pre-installed database of MySQL Server
RUN rm -rf /var/lib/mysql/*

# Add MySQL configuration
ADD my.cnf /etc/mysql/conf.d/my.cnf

# Script for creating the MySQL User
ADD mysql_user.sh /mysql_user.sh

# Script for running the files
ADD run.sh /run.sh

# Give the execution permission
RUN chmod 755 /*.sh

# Enviroment variable for setting the Username and Password of MySQL
ENV MYSQL_USER root
ENV MYSQL_PASS root

# Add VOLUMES
VOLUME  ["/etc/mysql", "/var/lib/mysql"]

# Set the port
EXPOSE 3306

# Execute the run.sh file
CMD ["/run.sh"]

