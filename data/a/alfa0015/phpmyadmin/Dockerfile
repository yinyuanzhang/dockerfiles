FROM phpmyadmin/phpmyadmin:latest
RUN sed -s -i -e "s/80/8080/" /etc/apache2/ports.conf /etc/apache2/sites-available/*.conf
EXPOSE 8080
