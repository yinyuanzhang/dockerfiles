FROM klimentdrv/ce-base-backend:latest

COPY ./docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN mkdir -p /var/log/supervisor

COPY ./ /var/www/html

RUN mv /var/www/html/.env.build.dev /var/www/html/.env

RUN mkdir -p resources/views/docs && rm -rf resources/views/docs/api.php || true
RUN raml2html ./api-docs/api.raml > resources/views/docs/api.php

RUN chmod -R 777 /var/www/html/bootstrap && chmod -R 777 /var/www/html/storage

RUN wget https://getcomposer.org/download/1.2.0-RC/composer.phar

VOLUME ["/var/www/html/vendor", "/var/www/html/node_modules", "/var/www/html/public/bower_components", "/var/www/html/public/compiled"]

EXPOSE 80
EXPOSE 443

CMD ["/usr/bin/supervisord"]