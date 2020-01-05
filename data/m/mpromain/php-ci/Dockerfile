FROM ubuntu:xenial

# apt-get set sources for PHP 7.0
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >> /etc/apt/sources.list \
	&& echo "deb-src http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >> /etc/apt/sources.list \
	&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 14AA40EC0831756756D7F66C4F4EA0AAE5267A6C

# install dependencies
RUN apt-get update
RUN apt-get install -y \
	curl \
	wget

# install version control systems
RUN apt-get install -y \
      git git-core \
      subversion \
      mercurial

# apt-get install php
RUN apt-get install -y \
	php7.0 \
	php7.0-cgi \
	php7.0-cli \
	php7.0-common \
	php7.0-curl \
	php7.0-fpm \
	php7.0-gd \
	php7.0-imagick \
	php7.0-interbase \
	php7.0-json \
	php7.0-mbstring \
	php7.0-mysql \
	php7.0-readline \
	php7.0-redis \
	php7.0-sqlite \
	php7.0-phpdbg \
	php7.0-xdebug \
	php7.0-xsl \
	php7.0-zip

RUN sed -i "s/^/;/g" /etc/php/7.0/cli/conf.d/20-xdebug.ini

# test PHP version
RUN php -r "if(version_compare(PHP_VERSION, '7.0.0', '<') || version_compare(PHP_VERSION, '7.1.0', '>=')){ echo 'Invalid PHP version '.PHP_VERSION; exit(1); }"

# Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Global composer packages
RUN composer global require \
	phpunit/phpunit \
	nette/tester \
	mockery/mockery \
	jakub-onderka/php-parallel-lint \
	jakub-onderka/php-console-highlighter \
	phpstan/phpstan

# Add composer binaries to paths
RUN echo "export PATH=\$PATH:\$HOME/.composer/vendor/bin/" >> ~/.bashrc
