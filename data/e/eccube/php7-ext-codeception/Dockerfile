FROM codeception/codeception

MAINTAINER Kentaro Ohkouchi <nanasess@fsm.ne.jp>

RUN mkdir -p /usr/share/man/man1 /usr/share/man/man7
RUN apt-get update && apt-get install --no-install-recommends -y \
        git curl wget sudo libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libmcrypt-dev libxml2-dev libpq-dev libpq5 postgresql-client mysql-client libicu-dev \
        && docker-php-ext-configure \
        gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
        && docker-php-ext-install -j$(nproc) \
        mbstring zip gd xml pdo pdo_pgsql pdo_mysql soap intl \
        && rm -r /var/lib/apt/lists/*
