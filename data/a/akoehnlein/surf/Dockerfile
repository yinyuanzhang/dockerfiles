FROM composer:1 AS composer

FROM debian:buster-slim

# add php package resources
RUN apt-get update \
	&& apt-get install apt-transport-https gnupg curl -y \
	&& curl https://packages.sury.org/php/apt.gpg | apt-key add - \
	&& echo 'deb https://packages.sury.org/php/ buster main' > /etc/apt/sources.list.d/php.list \
	&& apt-get update

# install non-php images
RUN apt-get install rsync git unzip npm nodejs -y

# install yarn
RUN curl -o- -L https://yarnpkg.com/install.sh | bash
ENV PATH "/root/.yarn/bin:/root/.config/yarn/global/node_modules/.bin:$PATH"

# install gulp-cli as global module
RUN yarn global add gulp-cli \
	&& touch ~/.dummy \
	&& yarn cache clean \
	&& rm -f ~/.dummy

# add php packages
RUN apt-get install php7.3-cli -y
RUN apt-get install php7.3-xml php7.3-gd php7.3-mbstring php7.3-curl php7.3-zip php7.3-mysqli php-xdebug -y

# install composer
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /tmp

# copy composer from official composer image
COPY --from=composer /usr/bin/composer /usr/bin/composer
ENV PATH "/tmp/vendor/bin:$PATH"

# Install typo3/surf
RUN composer global require typo3/surf:^2@dev \
    && composer clear-cache

# clean up
RUN apt-get clean

WORKDIR /app
CMD ["/bin/bash"]