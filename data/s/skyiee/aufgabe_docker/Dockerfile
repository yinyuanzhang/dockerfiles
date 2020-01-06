FROM php:apache
RUN docker-php-ext-install pdo pdo_mysql
COPY index.php /var/www/html

FROM mysql
COPY ./sql-scripts/ /docker-entrypoint-initdb.d/

EXPOSE 80