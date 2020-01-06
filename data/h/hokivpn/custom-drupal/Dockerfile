FROM       drupal:8.6.5
LABEL      maintainer="Daniel Chh"

# Instal PECL progressbar extension
#RUN pecl install uploadprogress-1.0.3.1 \
#    && docker-php-ext-enable uploadprogress
    
# Install PECL packages
#COPY docker-php-pecl-install /usr/local/bin/
#RUN chmod +x /usr/local/bin/docker-php-pecl-install
#RUN docker-php-pecl-install \
#uploadprogress-1.0.3.1 \

WORKDIR /var/www/html

EXPOSE 80
