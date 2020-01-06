FROM iwaydev/base-php-fpm-7.1-dev

WORKDIR /var/www/driver2

RUN apt-get -y clean && apt-get -y update

# PDF generator
RUN apt-get install -y xvfb wkhtmltopdf

RUN apt-get autoremove && \
    apt-get clean