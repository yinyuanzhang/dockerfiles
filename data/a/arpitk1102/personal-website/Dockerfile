############################################################
# Dockerfile to run a Django-based web application
# Based on an AMI
############################################################
# Set the base image to use to Ubuntu
FROM ubuntu:18.04
# Set the file maintainer (your name - the file's author)
MAINTAINER Arpit Khanna
# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKYARD)
# Local directory with project source
ENV DOCKYARD_SRC=code/blog
# Directory in container for all project files
#ENV DOCKYARD_SRVHOME=/srv
# Directory in container for project source files
ENV DOCKYARD_SRVPROJ=DOCKYARD_SRVHOME/$DOCKYARD_SRC
# Update the default application repository sources list
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python python3-pip
RUN apt-get install -y python-dev
RUN apt-get install -y libmysqlclient-dev
RUN apt-get install -y git
RUN apt-get install -y vim
RUN apt-get install -y mysql-server
RUN apt-get install -y nginx
# Create application subdirectories
WORKDIR /srv/code/blog
RUN mkdir static logs
#read
VOLUME ["/srv/code/blog/static/"]
# Copy application source code to SRCDIR
COPY /code/blog /srv/code/blog
# Install Python dependencies
RUN pip3 install -r /srv/code/blog/requirements.txt
# Port to expose
EXPOSE 80
# Copy entrypoint script into the image
WORKDIR /srv/code/blog
COPY ./docker-entrypoint.sh /
COPY ./django_nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/django_nginx.conf /etc/nginx/sites-enabled
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
ENTRYPOINT ["/docker-entrypoint.sh"]