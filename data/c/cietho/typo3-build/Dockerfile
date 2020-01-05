FROM php:7.2

RUN apt-get update \
    && apt-get install -y gnupg2 unzip rsync git ssh

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y nodejs yarn

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

