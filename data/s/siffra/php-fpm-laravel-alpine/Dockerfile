FROM        php:cli-alpine
LABEL maintainer="Luiz Benevenuto <luiz@siffra.com.br>"

# install commonly used php extensions
RUN apk add --update --no-cache \
	postgresql-dev libzip-dev freetype-dev \
    libpng-dev libjpeg-turbo-dev freetype \
    libpng libjpeg-turbo nodejs yarn \
    php7-bcmath php7-pcntl \
    openssh-client \
  && docker-php-ext-configure gd \
    --with-gd \
    --with-freetype-dir=/usr/include/ \
    --with-png-dir=/usr/include/ \
    --with-jpeg-dir=/usr/include/ && \
  NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
  && docker-php-ext-install -j${NPROC} gd pdo pdo_mysql pdo_pgsql opcache zip bcmath pcntl\
  && apk del --no-cache freetype-dev libpng-dev libjpeg-turbo-dev

# install composer
RUN apk add --update --no-cache \
  curl git zip unzip \
  && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
  && composer global require deployer/deployer deployer/recipes