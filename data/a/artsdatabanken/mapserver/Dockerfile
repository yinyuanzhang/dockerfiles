FROM camptocamp/mapserver
RUN a2enmod rewrite
RUN touch /var/log/mapserver.log
RUN chown www-data:www-data /var/log/mapserver.log
RUN mkdir -p /var/run/apache2
RUN chown -R www-data:www-data /var/run/apache2/

COPY docker/start-server /usr/local/bin/
COPY docker/000-default.conf /etc/apache2/sites-available/

EXPOSE 8080

RUN sed -i -e 's/<VirtualHost \*:80>/<VirtualHost *:8080>/' /etc/apache2/sites-available/000-default.conf
RUN sed -i -e 's/Listen 80$/Listen 8080/' /etc/apache2/ports.conf
