############################################################
# Dockerfile to build Nginx Installed Containers
# Based on Ubuntu 14.04
############################################################

# Set the base image to Ubuntu
FROM ubuntu:trusty

# File Author / Maintainer
MAINTAINER Maintaner khemlabs

# Install Nginx

# Update the repository
RUN apt-get update

# Install necessary tools
RUN apt-get install -y --no-install-recommends vim wget

# Download and Install Nginx
RUN apt-get install -y --no-install-recommends nginx

# Remove the default Nginx configuration file
RUN rm -v /etc/nginx/nginx.conf

# forward request and error logs to docker log collector
RUN 	ln -sf /dev/stdout /var/log/nginx/access.log && \
	ln -sf /dev/stderr /var/log/nginx/error.log

# Copy a configuration file from the current directory
ADD etc/nginx.conf /etc/nginx/

# Copy application folder and configurations
COPY vhost.d/* /etc/nginx/vhost.d/

# Append "daemon off;" to the beginning of the configuration
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80 443

# Set the default command to execute
# when creating a new container
CMD ["nginx"]
