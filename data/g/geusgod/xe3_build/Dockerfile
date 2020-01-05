FROM ubuntu:latest
LABEL "maintainer"="geusgod"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install php php-fpm php-mbstring php-dom php-zip php-pdo php-tokenizer php-xml php-ctype php-json php-mysql php-curl php-gd php-cgi php-cli -y
RUN apt-get install curl git apache2 -y
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

WORKDIR /var/www
RUN git clone https://github.com/xpressengine/xpressengine.git

WORKDIR /var/www/xpressengine
RUN composer install

RUN chgrp -R www-data /var/www/xpressengine
RUN chmod -R 775 /var/www/xpressengine

ADD xe.conf /etc/apache2/sites-available

RUN a2dissite 000-default.conf
RUN a2ensite xe.conf
RUN a2enmod rewrite
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
RUN service apache2 restart

CMD apachectl -DFOREGROUND