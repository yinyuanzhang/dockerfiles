FROM klimentdrv/base-frontend:latest

VOLUME ["/var/www/html/node_modules"]

COPY ./docker/nginx.conf /etc/nginx/

EXPOSE 80
EXPOSE 443

RUN mkdir -p /var/www && mkdir -p /var/www/html

WORKDIR /var/www/html

COPY ./ /var/www/html

CMD ["/usr/bin/supervisord"]
