FROM php:alpine

# Install dev dependencies
RUN apk add --no-cache --virtual .build-deps \
    $PHPIZE_DEPS \
    curl-dev \
    imagemagick-dev \
    libtool \
    libxml2-dev \
    postgresql-dev \
    sqlite-dev

# Install production dependencies
RUN apk add --no-cache \
    bash \
    curl \
    g++ \
    gcc \
    git \
    imagemagick \
    libc-dev \
    libpng-dev \
    make \
    mysql-client \
    nodejs \
    nodejs-npm \
    openssh-client \
    postgresql-libs \
    rsync \
    imap-dev \
    zlib-dev


# Install PECL and PEAR extensions
RUN pecl channel-update pecl.php.net

RUN pecl install \
    imagick \
    xdebug
RUN pear install PHP_CodeSniffer

# Install and enable php extensions
RUN docker-php-ext-enable \
    imagick \
    opcache \
    xdebug
RUN docker-php-ext-install \
    curl \
    iconv \
    mbstring \
    pdo \
    pdo_mysql \
    pdo_pgsql \
    pdo_sqlite \
    pcntl \
    tokenizer \
    xml \
    gd \
    zip \
    bcmath

RUN docker-php-ext-configure imap --with-imap --with-imap-ssl \
    && docker-php-ext-install imap

# Install composer
RUN curl -s https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin/ --filename=composer
ENV COMPOSER_ALLOW_SUPERUSER=1
ENV PATH="./vendor/bin:$PATH"

# Cleanup dev dependencies
RUN apk del -f .build-deps

# Setup working directory
WORKDIR /var/www
