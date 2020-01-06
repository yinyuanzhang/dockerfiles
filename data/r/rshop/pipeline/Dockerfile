FROM rshop/install:7.3

RUN apt-get update && apt-get install -y \
        apt-transport-https \
        gnupg2 \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update && ACCEPT_EULA=Y apt-get install -y \
        msodbcsql17 \
        mssql-tools \
        unixodbc-dev \
    && pecl install sqlsrv \
    && docker-php-ext-enable sqlsrv \
    && pecl install pdo_sqlsrv \
    && docker-php-ext-enable pdo_sqlsrv \
    && curl -sL https://cs.sensiolabs.org/download/php-cs-fixer-v2.phar > /usr/bin/php-cs-fixer \
    && chmod a+x /usr/bin/php-cs-fixer \
    && pecl install swoole \
    && docker-php-ext-enable swoole
