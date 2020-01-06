FROM php:7.2-fpm

# Install Postgre PDO
RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y --no-install-recommends \
		build-essential \
		libpq-dev \
		curl \
		gnupg \
		gnupg2 \
		gnupg1 \
		zip \
		git \
		unzip \
		libzip-dev \
		libfreetype6-dev \
		libjpeg62-turbo-dev \
		libmemcached-dev \
	    libz-dev \
	    libpq-dev \
	    libjpeg-dev \
	    libpng-dev \
	    libfreetype6-dev \
	    libssl-dev \
		libmcrypt-dev \
		&& rm -rf /var/lib/apt/lists/*

# Install the PHP pdo_mysql extention
RUN docker-php-ext-configure zip --with-libzip \
	&& docker-php-ext-install pdo pdo_pgsql zip \
	&& docker-php-ext-configure gd \
		--with-jpeg-dir=/usr/lib \
		--with-freetype-dir=/usr/include/freetype2 && \
	docker-php-ext-install gd

# install composer
RUN curl -sSL --show-error https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# install node and npm
RUN curl -sSL --show-error https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs

# copy files
COPY server/gpm/sites-available /etc/apache2/sites-available
COPY server/gpm/sites-enabled /etc/apache2/sites-enabled
COPY --chown=www-data:www-data web /var/www/html
COPY env/gpm/.env /var/www/html/

WORKDIR /var/www/html
# RUN composer install && npm i && npm run prod
RUN npm i && npm run prod
# RUN php artisan key:generate