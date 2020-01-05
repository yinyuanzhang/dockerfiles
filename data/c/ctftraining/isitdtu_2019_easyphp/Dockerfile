FROM ctftraining/base_image_nginx_php_73
COPY src/ /var/www/html/
COPY _files/php.ini /usr/local/etc/php/
COPY _files/nginx.conf /etc/nginx/
COPY _files/flag.sh /flag.sh
RUN chmod +x /flag.sh
