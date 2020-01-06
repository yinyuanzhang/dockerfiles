# Docker file for Angular ESPN API App

# DOCKER-VERSION 1.0

# Base image
FROM centos:6.4

# Who?
MAINTAINER J. Scott Elson, aguyawry@gmail.com

# Node.js and npm are available from the Fedora Extra Packages for Enterprise Linux (EPEL) repository.
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
RUN yum install -y npm

# Add the app
ADD . /src

# Install dependencies
RUN cd /src; npm install

# Expose port
EXPOSE  8002

CMD ["npm", "start"]