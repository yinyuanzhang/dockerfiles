FROM php:7.2-apache

LABEL Rufus Mbugua - https://github.com/rufusmbugua

# If you want to use the image to deploy your source code uncomment the next line
# COPY . /var/www/html/
COPY ./docker/000-default.conf /etc/apache2/sites-available/000-default.conf

# Prepare MySQL
RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections 
RUN echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections 


# Install Additional Packages
RUN apt-get update 
RUN apt-get install --no-install-recommends -y mysql-server git zip unzip libmcrypt-dev zlib1g-dev libicu-dev g++
RUN docker-php-ext-configure intl
RUN docker-php-ext-install pdo pdo_mysql intl pcntl
RUN pecl install mcrypt-1.0.1
RUN docker-php-ext-enable mcrypt pcntl
RUN a2enmod rewrite
RUN service apache2 restart
RUN service mysql start

# Install Composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  \
	&&	php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
	&& 	php composer-setup.php --install-dir=/bin   --name=composer \
	&& 	php -r "unlink('composer-setup.php');" \
	&& 	mv /bin/composer.phar /usr/local/bin/composer

# Install Composer Packages
RUN composer self-update

VOLUME ["/var/www/html"]

WORKDIR /var/www/html

EXPOSE 80/tcp
EXPOSE 80/udp
