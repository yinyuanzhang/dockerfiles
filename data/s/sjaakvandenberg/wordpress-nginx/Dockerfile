FROM nginx:alpine

COPY nginx.conf         /etc/nginx/nginx.conf
COPY vhost.conf         /etc/nginx/sites-enabled/vhost.conf
COPY index.php          /var/www/wordpress/

RUN set +x \
apk add --no-cache curl \
&& addgroup -g 82 -S www-data \
&& adduser -u 82 -D -S -G www-data www-data \
&& ln -sf /dev/stdout /var/log/nginx/access.log \
&& ln -sf /dev/stderr /var/log/nginx/error.log \
&& rm /etc/nginx/conf.d/default.conf \
&& chown -R www-data:www-data /etc/nginx/conf.d/ /etc/nginx/nginx.conf /usr/sbin/nginx

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
