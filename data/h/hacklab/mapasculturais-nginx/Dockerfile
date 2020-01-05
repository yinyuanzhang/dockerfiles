FROM nginx:mainline

COPY nginx.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /var/www/html
RUN touch /var/www/html/index.php
RUN chown www-data:www-data -R /var/www
