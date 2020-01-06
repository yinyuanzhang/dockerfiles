FROM php:5.6-cli-jessie

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -

# Install packages
RUN apt-get update && apt-get install -qy git curl libmcrypt-dev mysql-client unzip libxml2-dev zlib1g-dev sqlite3 p7zip-full openssh-client rsync nodejs libgmp-dev libpng-dev wget
RUN apt-get clean -y

# Install xdebug extension
RUN wget https://xdebug.org/files/xdebug-2.5.5.tgz && tar -xf xdebug-2.5.5.tgz
RUN cd xdebug-2.5.5 && phpize && ./configure --enable-xdebug && make && cp modules/xdebug.so /usr/local/lib/php/extensions/no-debug-non-zts-20131226
RUN echo 'zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20131226/xdebug.so' > /usr/local/etc/php/conf.d/xdebug-php.ini

# Install other php extensions
RUN docker-php-ext-install soap
RUN ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/local/include/
RUN docker-php-ext-configure gmp
RUN docker-php-ext-install gmp
RUN docker-php-ext-install zip

## Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

## Install Deployer with recipes
RUN composer global require deployer/deployer
RUN composer global require deployer/recipes --dev

## Add Composer vendor into PATH
ENV PATH /root/.composer/vendor/bin:$PATH

COPY "memory-limit-php.ini" "/usr/local/etc/php/conf.d/memory-limit-php.ini"