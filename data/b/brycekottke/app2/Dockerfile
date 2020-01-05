#
# Nginx Dockerfile
#
# https://github.com/dockerfile/nginx
#

# Pull base image.
FROM ubuntu:14.04

# Install Nginx.
RUN \
  apt-get update && \
  apt-get install -y software-properties-common python-software-properties && \
  add-apt-repository -y ppa:nginx/stable && \
  apt-get update && \
  apt-get install -y nginx && \
  rm -rf /var/lib/apt/lists/* && \
  echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
  chown -R www-data:www-data /var/lib/nginx && \
  mkdir -p /var/www/html && \
  mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.old && \
  mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.old && \
  rm /var/www/html/* && \
  rm /etc/nginx/sites-enabled/*

ADD nginx.conf /etc/nginx/
ADD default /etc/nginx/sites-available/
ADD index.html /var/www/html/

RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

# Define mountable directories.
#VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx", "/var/www/html"]

# Define working directory.
WORKDIR /etc/nginx

# Define default command.
CMD ["nginx"]

# Expose ports.
EXPOSE 80
#EXPOSE 443
