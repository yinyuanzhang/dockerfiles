FROM richarvey/nginx-php-fpm:1.5.7
RUN apk add npm yarn && composer global require hirak/prestissimo
ADD ./hserv /var/www/html/hserv
ADD ./conf /var/www/html/conf
ADD ./scripts /var/www/html/scripts
RUN cd /var/www/html/hserv/ && ./updateFront.sh && composer install -o
ENV REMOVE_FILES 0
ENV SKIP_CHOWN 1
ENV ENABLE_XDEBUG 0
ENV APPLICATION_ENV production
ENV APP_ENV prod
ENV RUN_SCRIPTS 1