FROM nginx:latest

WORKDIR /etc/nginx

COPY nginx.conf .
COPY symfony.conf ./sites-available/symfony.conf

RUN rm ./conf.d/default.conf
RUN echo "upstream php-upstream { server php:9000; }" > ./conf.d/upstream.conf
RUN usermod -u 1000 www-data