FROM php:5.5-cli
# Install modules
RUN    docker-php-ext-configure mysql --with-libdir=lib/x86_64-linux-gnu/ \
    && docker-php-ext-install mysql
RUN    docker-php-ext-configure mysqli --with-libdir=lib/x86_64-linux-gnu/ \
    && docker-php-ext-install mysqli
CMD ["php", "-a"]
