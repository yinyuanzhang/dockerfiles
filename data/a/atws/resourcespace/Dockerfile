FROM richarvey/nginx-php-fpm:1.8.2

RUN apk add --no-cache \
	imagemagick \
	ghostscript \
	ffmpeg \
	exiftool \
	antiword \
	poppler-utils \
	mysql-client

COPY files/ /var/www/html/

VOLUME ["/var/www/html/filestore"]


WORKDIR /var/www/html
