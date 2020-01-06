FROM ubuntu

MAINTAINER duykhoa95 <duykhoa95@gmail.com>

RUN apt-get update -y && \
    apt-get install -y \
	php-fpm php-mysql

VOLUME [ "/var/www/html" ]
WORKDIR /var/www/html
EXPOSE 9000
CMD ["php7-fpm.0"]
