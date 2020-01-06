FROM php:7.4-rc-cli-alpine3.10 as php

WORKDIR /var/s3sftp

########################################################################################################################
##
## COMPOSER
##
########################################################################################################################
FROM php AS composer

RUN apk add  --no-cache \
      curl \
      unzip  \
   && rm -rf /var/lib/apt/lists/*

# Install composer
COPY ./composer-installer.sh /usr/local/bin/composer-installer

RUN chmod +x /usr/local/bin/composer-installer \
    && /usr/local/bin/composer-installer \
    && mv composer.phar /usr/local/bin/composer \
    && chmod +x /usr/local/bin/composer \
    && /usr/local/bin/composer global require hirak/prestissimo -n

########################################################################################################################
##
## COMPOSER INSTALL
##
########################################################################################################################
FROM composer AS composer_install

COPY ./composer.json /var/s3sftp/composer.json
COPY ./composer.lock /var/s3sftp/composer.lock

RUN /usr/local/bin/composer install -o -v

########################################################################################################################
##
## FINAL
##
########################################################################################################################
FROM php AS final

# VENDOR DIRECTORY
COPY --from=composer_install /var/s3sftp/vendor /var/s3sftp/vendor

COPY ./app /var/s3sftp/app
COPY ./s3sftp.php /var/s3sftp/s3sftp.php

RUN chmod +x /var/s3sftp/s3sftp.php

ENTRYPOINT ["/var/s3sftp/s3sftp.php"]
