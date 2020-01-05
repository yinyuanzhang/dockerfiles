FROM        php:cli
LABEL maintainer="Luiz Benevenuto <luiz@siffra.com.br>"

# Install modules
RUN buildDeps="libpq-dev libzip-dev libicu-dev xml2 libxml2-dev git curl ssh-client unzip libmagickwand-dev gnupg2 sudo curl apt-transport-https" && \
    apt-get update && apt-get install -fy $buildDeps --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* && \
    pecl install imagick && \
    docker-php-ext-install \
        zip \
        gd \
        mbstring \
        tokenizer \
        xml \
        pdo \
        pdo_pgsql \
        pgsql \
        sockets \
        intl \
        bcmath \
        pcntl && \
    docker-php-ext-enable imagick

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -fy yarn --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php composer-setup.php --install-dir=/bin --filename=composer
RUN composer global require deployer/deployer deployer/recipes

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update && \
    apt-get install -fy nodejs --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* && \
    apt autoremove -fy