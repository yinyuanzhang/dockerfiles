FROM php:apache
RUN ["chmod", "-R", "755", "/var/www/html"]
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli

RUN apt-get update && \
    apt-get install -y libfreetype6-dev libjpeg62-turbo-dev && \
    docker-php-ext-install mysqli && \
    docker-php-ext-install mbstring && \
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/  &&  \
    docker-php-ext-install gd

COPY ssl/certificate.crt /etc/apache2/ssl_keys/server.crt
COPY ssl/private.key /etc/apache2/ssl_keys/server.key
COPY ssl/GLOBALSIGN_ORGANIZATION_VALIDATION_CA__SHA256__G.crt /etc/apache2/ssl_keys/ChainBundle.crt
COPY ssl/GLOBALSIGN_ROOT_CA.crt /etc/apache2/ssl_keys/ROOT.crt
COPY ssl/pass.sh /etc/apache2/ssl_keys/pass.sh
RUN chmod 777 /etc/apache2/ssl_keys/pass.sh

COPY . /var/www/html

ADD ssl/ssl.conf /etc/apache2/sites-available/ssl.conf                                 
ADD ssl/entrypoint.sh /opt/entrypoint.sh                                               

RUN chmod a+x /opt/entrypoint.sh
RUN a2enmod ssl
RUN a2ensite ssl

RUN ["chmod", "-R", "777", "/var/www/html/common/htmlpurifier-4.9.3"]
WORKDIR /var/www/html

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

EXPOSE 80 443