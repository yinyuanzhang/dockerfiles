FROM aesopagency/base:ubuntu-14.04

MAINTAINER Aesop Agency <technical@aesopagency.com>

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /tmp

# Install Nginx
RUN apt-get update -y && \
    apt-get install -y nginx

# Apply Nginx configuration
ADD config/nginx.conf /opt/etc/nginx.conf
ADD config/vhost /opt/etc/vhost

# Nginx startup script
ADD config/nginx-start.sh /opt/bin/nginx-start.sh
RUN chmod u=rwx /opt/bin/nginx-start.sh

# PORTS
EXPOSE 80
EXPOSE 443

WORKDIR /opt/bin
ENTRYPOINT ["/opt/bin/nginx-start.sh"]
