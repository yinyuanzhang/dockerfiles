FROM docker:stable-git
RUN apk add --update --no-cache \
  php-cli \
  php-curl \
  php-xml \
  php-mbstring \
  php-bz2 \
  php-gd \
  unzip \
  php-json \
  php-phar \
  php-openssl \
  php-simplexml \
  php-dom \
  php-xmlwriter \
  php-bcmath \
  php-tokenizer \
  php-pdo \
  php-session \
  php-ctype \
  php-fileinfo \
  openssl \
  git \
  subversion \
  openssh \
  mercurial \
  tini \
  bash \
  patch \
  make \
  zip \
  unzip; \
  \
# Install composer
  wget -qO- https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer; \
  \
  composer global require "hirak/prestissimo:^0.3";
