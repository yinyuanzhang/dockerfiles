FROM php:7.3-fpm
LABEL Maintainer = Kevin ARBOUIN dev@arbouin-consulting.com
LABEL Name = PHP FPM development

RUN apt-get update \
    && apt-get install --no-install-recommends -yqq \
        vim \
        libicu-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        zlib1g-dev \
        git git-core \
        gcc make autoconf libc-dev pkg-config \
        zlib1g-dev \
        curl \
        wget \
        python \
        python-pip \
        unzip \
        libpng-dev \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libxrender1 \
        libfontconfig \
        librabbitmq-dev \
        libxtst6 \
        libxml2-dev \
        xz-utils \
        libzip-dev \
        mongo-tools \
        sudo \
        ssh \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN curl "https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz" -L -o "wkhtmltopdf.tar.xz" \
    && tar Jxvf wkhtmltopdf.tar.xz \
    && mv wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf \
    && rm -rf wkhtmltopdf.tar.xz wkhtmltox/ \
    && docker-php-ext-install \
        opcache \
        intl \
        mbstring \
        pdo_mysql \
        zip \
        json \
        curl \
        sockets \
        bcmath \
        gd \
        soap \
        pcntl
RUN pecl install xdebug mongodb \
    && echo "extension=mongodb.so" >> /usr/local/etc/php/conf.d/mongodb.ini \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && pecl install amqp \
    && docker-php-ext-enable amqp \
    && php -r "readfile('https://getcomposer.org/installer');" | php -- --install-dir=/usr/local/bin --filename=composer \
    && chmod +x /usr/local/bin/composer \
    && apt-get clean \
    && rm -rf /root/.composer/cache/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && apt-get remove -y \
        vim \
        python \
        python-pip \
    && apt-get clean \
    && rm -rf /root/.composer/cache/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN groupadd appuser \
    && useradd -m -r -u 1000 -g appuser appuser \
    && mkdir -p /home/appuser/ \
    && chown -R appuser:appuser /home/appuser/ \
    && chmod -R 0711 /home/appuser/ \
    && echo 'export PATH=$HOME/bin:/usr/local/bin:/usr/local/sbin:$HOME/.composer/vendor/bin:$PATH' >> /home/appuser/.bashrc \
    && echo "alias sf='bin/console'" >> /home/appuser/.bashrc \
    && echo "alias ls='ls --color'" >> /home/appuser/.bashrc \
    && echo "alias ll='ls -l'" >> /home/appuser/.bashrc \
    && echo "alias la='ls -la'" >> /home/appuser/.bashrc \
    && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER appuser

ENV TERM=xterm
