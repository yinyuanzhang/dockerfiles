FROM php:7.2-cli

ENV IGBINARY_VERSION=2.0.5
ENV XDEBUG_VERSION=2.6.0

RUN apt-get update && \
    apt-get install \
        curl \
        git \
        zip \
        unzip \
        build-essential \
        jpegoptim \
        librsvg2-dev \
        libmagickwand-dev \
        libreadline-dev \
        libedit-dev \
        libcurl3-dev \
        libicu-dev \
        libxml2-dev \
        libsqlite3-dev \
        libtidy-dev \
        vim \
        zsh \
    --no-install-recommends -y

RUN cd ~ \
    && git clone git://github.com/bwithem/oh-my-zsh.git ~/.oh-my-zsh \
    && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \
    && sed -e 's~ZSH_THEME~#ZSH_THEME~' -i ~/.zshrc \
    && curl https://codeload.github.com/Bukashk0zzz/vimrc/zip/master > vim.zip \
    && unzip vim.zip \
    && cp -r vimrc-master/.vim* . \
    && rm vim.zip \
    && rm -rf vimrc-master

RUN docker-php-ext-install \
    pdo readline zip opcache soap curl intl json sockets gd \
    pdo_mysql pdo_sqlite mbstring bcmath tidy xml 2>&1 > /dev/null

ADD https://github.com/awslabs/aws-elasticache-cluster-client-libmemcached/archive/master.zip /tmp
RUN cd /tmp \
    && unzip master.zip \
    && cd /tmp/aws-elasticache-cluster-client-libmemcached-master \
    && mkdir BUILD \
    && touch configure.ac aclocal.m4 configure Makefile.am Makefile.in \
    && cd BUILD \
    && ../configure --prefix=/usr/include/ --with-pic \
    && make \
    && make install

ADD https://github.com/igbinary/igbinary/archive/${IGBINARY_VERSION}.zip /tmp
RUN cd /tmp \
    && unzip ${IGBINARY_VERSION}.zip \
    && cd /tmp/igbinary-${IGBINARY_VERSION} \
    && phpize \
    && ./configure \
    && make \
    && make test \
    && make install \
    && docker-php-ext-enable igbinary

ADD https://github.com/awslabs/aws-elasticache-cluster-client-memcached-for-php/archive/php7.zip /tmp
RUN cd /tmp \
    && unzip php7.zip \
    && cd /tmp/aws-elasticache-cluster-client-memcached-for-php-php7 \
    && phpize \
    && ./configure --with-libmemcached-dir=/usr/include/ --disable-memcached-sasl --enable-memcached-igbinary \
    && make \
    && make install \
    && docker-php-ext-enable memcached

ADD https://github.com/xdebug/xdebug/archive/${XDEBUG_VERSION}.zip /tmp
RUN cd /tmp \
    && unzip ${XDEBUG_VERSION}.zip \
    && cd /tmp/xdebug-${XDEBUG_VERSION} \
    && phpize \
    && ./configure \
    && make \
    && make test \
    && make install

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php \
    && php -r "unlink('composer-setup.php');" \
    && mv composer.phar /usr/local/bin/composer

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
ENV TERM xterm-256color

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/*  /tmp/*

COPY conf/php.ini /usr/local/etc/php/php.ini
COPY conf/xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini
COPY docker-entrypoint.sh /

RUN chmod +x /usr/local/bin/composer /docker-entrypoint.sh
RUN mkdir -p /app/var
WORKDIR /app

ENTRYPOINT ["/docker-entrypoint.sh"]
