FROM initlab/composer
MAINTAINER Roman Agabekov <r.agabekov@gmail.com>

RUN echo "phar.readonly = 0" >> /usr/local/etc/php/php.ini

RUN composer create-project "squizlabs/php_codesniffer=2.0.*@dev"
RUN php php_codesniffer/scripts/build-phar.php
RUN chmod +x *.phar

RUN mv phpcbf.phar  /usr/local/bin/phpcbf
RUN mv phpcs.phar   /usr/local/bin/phpcs

RUN rm -rf php_codesniffer
RUN rm -rf /usr/local/bin/composer

CMD ["phpcbf"]
CMD ["phpcs"]
