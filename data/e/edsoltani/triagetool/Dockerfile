FROM php:7.3.9-apache
#install all the dependencies
RUN apt-get update && apt-get install -y \
  build-essential \ 
  libssl-dev \
  libicu-dev \
  libpq-dev \
  libmcrypt-dev \
  libzip-dev \
  git \
  zip \
  unzip \
  && rm -r /var/lib/apt/lists/* \
  && docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \
  && docker-php-ext-install \
  intl \
  mbstring \
  pcntl \
  pdo_mysql \
  pdo_pgsql \
  pgsql \
  zip \
  opcache

#install composer
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

RUN apt-get update && apt-get install -y nodejs

ENV APP_HOME /var/www/html

#change uid and gid of apache to docker user uid/gid
RUN usermod -u 1000 www-data && groupmod -g 1000 www-data

#change apache setting
RUN sed -i -e "s/html/html\/public/g" /etc/apache2/sites-enabled/000-default.conf
RUN a2enmod rewrite

#copy source files and run composer
COPY . $APP_HOME

# install libraries
RUN composer install --no-interaction
RUN npm install

#change ownership
RUN chown -R www-data:www-data $APP_HOME

# Configure Triage Tool
RUN npm run dev
RUN php artisan migrate:install
RUN php artisan migrate --step
RUN php artisan db:seed
RUN php artisan config:cache

#change ownership
RUN chown -R www-data:www-data $APP_HOME