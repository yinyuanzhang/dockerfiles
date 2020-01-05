#################################
#   LINE Wordpress Dockerfile   #
#################################

FROM wordpress:php7.1-apache

LABEL maintainer="Pornjed Sakgitjarung <pornjeds@skooldio.com>"

RUN echo 'COPYING requires files'
COPY ./public /var/www/html
COPY ./line-theme /var/www/html/wp-content/themes/line-learning-theme
COPY ./plugins /var/www/html/wp-content/plugins
COPY ./uploads /var/www/html/wp-content/uploads

RUN echo 'changing www permission for apache'
RUN chown -R www-data:www-data /var/www

EXPOSE 80
EXPOSE 443
