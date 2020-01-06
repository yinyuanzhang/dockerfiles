FROM eboost/php7fpm

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "if (hash_file('SHA384', 'composer-setup.php') === 'aa96f26c2b67226a324c27919f1eb05f21c248b987e6195cad9690d5c1ff713d53020a02ac8c217dbf90a7eacc9d141d') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
    && php -r "unlink('composer-setup.php');"

RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN apt-get update && apt-get install -y \
    git-core \
    curl \
    build-essential \
    openssl \
    libssl-dev \
    nodejs \
    ruby-full \
    rubygems-integration \
    graphicsmagick \
    openssh-client \
    sshpass

RUN gem install sass \
    && gem install bundler

RUN npm install -g gulp \
    && npm install -g bower \
    && npm install -g yarn
