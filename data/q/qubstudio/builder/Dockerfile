FROM php:7.2-cli

MAINTAINER kuzyk <andriy.kuzyk@qubstudio.com>

RUN apt-get update && apt-get install apt-transport-https curl software-properties-common gnupg -y

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -

RUN apt-get install -y \
		autoconf automake libtool nasm make \
		libpng-dev \
        openssh-client \
		curl \
		wget \
		zip \
		rsync \
		unzip \
		nodejs \
		git \
		yarn \
		libicu-dev
		
RUN php -m

RUN docker-php-ext-configure intl \
        && docker-php-ext-install intl \
		&& docker-php-ext-enable intl

RUN docker-php-ext-configure exif \
        && docker-php-ext-install exif \
		&& docker-php-ext-enable exif

RUN docker-php-ext-configure gd \
        && docker-php-ext-install gd \
		&& docker-php-ext-enable gd

RUN docker-php-ext-configure zip \
        && docker-php-ext-install zip \
		&& docker-php-ext-enable zip

RUN echo "export PATH=$PATH:`yarn global bin`" >> ~/.bashrc

RUN yarn global add gulp

RUN curl https://getcomposer.org/composer.phar -Ls --output /usr/bin/composer
RUN chmod +x /usr/bin/composer

RUN curl https://deployer.org/deployer.phar -Ls --output /usr/bin/deployer
RUN chmod +x /usr/bin/deployer

ENTRYPOINT ["deployer", "composer"]

CMD ["--version"]
