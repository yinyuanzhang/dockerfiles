FROM php:7.2.4-apache-stretch

RUN apt-get update

ADD ./football-bets.conf /etc/apache2/sites-available/

RUN a2enmod rewrite headers expires deflate
RUN a2dissite 000-default.conf && a2ensite football-bets.conf

RUN apt-get install -y libwebp-dev libjpeg62-turbo-dev libpng-dev libxpm-dev \
    libfreetype6-dev node-less git

# NODEJS
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -y nodejs

 # YARN
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
apt-get update && apt-get install yarn -y

# YARN packages
RUN yarn add @symfony/webpack-encore --dev
RUN yarn add sass-loader@^7.0.1 node-sass --dev

RUN docker-php-ext-configure gd --with-gd --with-webp-dir --with-jpeg-dir \
    --with-png-dir --with-zlib-dir --with-xpm-dir

RUN docker-php-ext-install pdo_mysql gd zip

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer --version=1.7.2

WORKDIR /var/www/football-bets