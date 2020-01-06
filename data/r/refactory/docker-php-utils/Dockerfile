FROM php:7.2

ENV GIT_LFS_VERSION=2.3.4

RUN apt-get update -yqq

RUN apt-get install git gnupg openssh-client unzip ansible libcurl4-gnutls-dev libicu-dev libmcrypt-dev libvpx-dev libjpeg-dev libpng-dev libxpm-dev zlib1g-dev libfreetype6-dev libxml2-dev libexpat1-dev libbz2-dev libgmp3-dev libldap2-dev unixodbc-dev libpq-dev libsqlite3-dev libaspell-dev libsnmp-dev libpcre3-dev libtidy-dev wget openssh-server apt-transport-https ca-certificates -yqq
RUN apt-get install sqlite3 libsqlite3-dev -yqq
RUN export CFLAGS="$PHP_CFLAGS" CPPFLAGS="$PHP_CPPFLAGS" LDFLAGS="$PHP_LDFLAGS" \
    && apt-get install -y --no-install-recommends \
        libmagickwand-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pecl install imagick-3.4.3    

RUN ansible-galaxy install ansistrano.deploy,1.12.0 ansistrano.rollback,1.5.0
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install pdo pdo_mysql pdo_sqlite gd zip simplexml mbstring curl json intl xml bz2 opcache
RUN pecl install xdebug

# Add git lfs
RUN curl -Lo git-lfs.tar.gz https://github.com/git-lfs/git-lfs/releases/download/v${GIT_LFS_VERSION}/git-lfs-linux-amd64-${GIT_LFS_VERSION}.tar.gz \
    && tar xzf git-lfs.tar.gz && cd git-lfs-${GIT_LFS_VERSION} && ./install.sh && cd .. && rm -rf git-lfs*
# Add composer
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer && echo 'export PATH="$PATH:$HOME/.composer/vendor/bin"' >> ~/.bashrc
# Add xml-linter
RUN composer global require mickaelandrieu/xml-linter
# Add phpunit
RUN curl -Lo /usr/local/bin/phpunit https://phar.phpunit.de/phpunit.phar && chmod +x /usr/local/bin/phpunit
# Add php-cs-fixer
RUN curl -Lo /usr/local/bin/php-cs-fixer http://cs.sensiolabs.org/download/php-cs-fixer-v2.phar && chmod +x /usr/local/bin/php-cs-fixer
# Add phpmd
RUN curl -Lo /usr/local/bin/phpmd http://static.phpmd.org/php/latest/phpmd.phar && chmod +x /usr/local/bin/phpmd
# Add phpcpd
RUN curl -Lo /usr/local/bin/phpcpd https://phar.phpunit.de/phpcpd.phar && chmod +x /usr/local/bin/phpcpd
# Add security-checker
RUN curl -Lo /usr/local/bin/security-checker http://get.sensiolabs.org/security-checker.phar && chmod +x /usr/local/bin/security-checker
# Add phpstan
RUN composer global require phpstan/phpstan-shim
# Add prestissimo
RUN composer global require hirak/prestissimo
# Add Surf
RUN composer global config minimum-stability beta && composer global require typo3/surf:^2.0.0
