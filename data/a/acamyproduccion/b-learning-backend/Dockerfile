#Comenzamos con la imagen base - version 7.1.5
FROM php:7.1.5-apache

#instala todas las dependencias del sistema y habilitar los módulos de PHP
RUN apt-get update && apt-get install -y \
      libicu-dev \
      libpq-dev \
      libmcrypt-dev \
      git \
      zip \
      unzip \
    && rm -r /var/lib/apt/lists/* \
    && docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \
    && docker-php-ext-install \
      intl \
      mbstring \
      mcrypt \
      pcntl \
      pdo_mysql \
      pdo_pgsql \
      pgsql \
      zip \
      opcache

#install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

#establece la carpeta de aplicaciones como una variable de entorno
ENV APP_HOME /var/www/html

#cambiar el uid y el gid de apache al usuario de la aplicación uid / gid
RUN usermod -u 1000 www-data && groupmod -g 1000 www-data

#cambia la raíz web_root a laravel / var / www / html / public folder
RUN sed -i -e "s/html/html\/public/g" /etc/apache2/sites-enabled/000-default.conf

# habilitar la reescritura del módulo apache
RUN a2enmod rewrite

#copiar archivos fuente y ejecutar compositor
COPY . $APP_HOME

# instalar todas las dependencias de PHP
RUN composer install --no-interaction

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
  apt-get install -y nodejs

#cambiar la propiedad de nuestras aplicaciones
RUN chown -R www-data:www-data $APP_HOME

#RUN chmod 755 $APP_HOME