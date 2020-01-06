FROM ubuntu
RUN apt-get update && apt-get install -y nginx
RUN rm -rf /var/www/html/*.html
COPY index.html /var/www/html/
CMD nginx -g 'daemon off;'
