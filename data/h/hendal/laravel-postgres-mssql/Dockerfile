FROM hendal/laravel-postgresql:7.2

RUN apt-get update \
  && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
  && curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list \
  && apt-get install -y --no-install-recommends locales apt-transport-https \
  && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen locale-gen \
  && apt-get update \
  && ACCEPT_EULA=y apt-get -y --no-install-recommends install unixodbc-dev msodbcsql17 \
  && curl -sL https://deb.nodesource.com/setup_12.x | bash - \
  && apt-get install nodejs -y \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

RUN pecl install sqlsrv pdo_sqlsrv \
  && docker-php-ext-enable sqlsrv pdo_sqlsrv

