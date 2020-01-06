FROM phusion/baseimage
EXPOSE 80

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

ENV PHP_UPLOAD_MAX_FILESIZE=512M
ENV PHP_POST_MAX_SIZE=512M

RUN apt-get update
RUN apt-get -o Dpkg::Options::="--force-confold" -y install \
         php7.0 \
         php7.0-zip \
         php7.0-mbstring \
         # php7.0-mysql \
         php7.0-pgsql \
         php7.0-gd \
         php7.0-curl \
         php7.0-imap \
         php7.0-xml \
         apache2 \
         libapache2-mod-php7.0 \
         bzip2
RUN sed -ri \
    -e "s/^upload_max_filesize.*/upload_max_filesize = ${PHP_UPLOAD_MAX_FILESIZE}/" \
    -e "s/^post_max_size.*/post_max_size = ${PHP_POST_MAX_SIZE}/" /etc/php/7.0/cli/php.ini

COPY limesurvey.tar.bz2 /
RUN tar xvjf /limesurvey.tar.bz2 \
    && rm /limesurvey.tar.bz2 \
    && rm -rf /var/www/html \
    && mv /limesurvey /var/www/html \
    && chown -R www-data:www-data /var/www/html \
    && chown www-data:www-data /var/lib/php \
    && mkdir /default_upload \
    && chown www-data:www-data /default_upload \
    && cp -r /var/www/html/upload/* /default_upload

COPY apache.service /etc/service/apache/run

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
