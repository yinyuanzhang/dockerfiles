FROM ubuntu:16.04
MAINTAINER "Ratan"
RUN apt-get update && apt install -y nginx
RUN rm -rf /var/www/html/*.*
COPY index.html /var/www/html/
EXPOSE 8080 8081
COPY index.html /var/www/html/
VOLUME ["/var/log/nginx"]
CMD nginx -g 'daemon off;'
