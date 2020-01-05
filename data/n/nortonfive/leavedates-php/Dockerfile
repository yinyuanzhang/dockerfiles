FROM php:7.2
RUN apt-get update && apt-get install -y libicu-dev libxml2-dev python-dev unzip \
		libfreetype6-dev \
		libjpeg62-turbo-dev \
		libpng-dev \
        libmcrypt-dev \
        zlib1g-dev \
        zip \
	&& docker-php-ext-install zip
RUN docker-php-ext-install -j$(nproc) iconv \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
	&& docker-php-ext-install -j$(nproc) intl \
	&& docker-php-ext-install -j$(nproc) mbstring \
	&& docker-php-ext-install -j$(nproc) pdo \
	&& docker-php-ext-install -j$(nproc) xml \
	&& docker-php-ext-install -j$(nproc) bcmath 
RUN curl -o /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py 
RUN python /tmp/get-pip.py 
RUN pip install awscli 
RUN pecl install xdebug 
RUN docker-php-ext-enable xdebug 
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer 

