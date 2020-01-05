FROM wordpress

RUN apt-get update && apt-get upgrade -y && apt-get install -y imagemagick exif

RUN chown -R www-data:root /var/www/html/

ADD ./php.ini /usr/local/etc/php/conf.d
