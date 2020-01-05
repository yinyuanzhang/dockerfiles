FROM php:7.1.11-apache-jessie
RUN set -e; \
  BUILD_PACKAGES="libzip-dev libssh2-1-dev unixodbc-dev"; \
  DEPS_PACKAGES="apt-transport-https locales"; \
  apt-get update; \
  apt-get install -y $DEPS_PACKAGES; \
  echo "en_US.UTF-8 UTF-8" > /etc/locale.gen; \ 
  locale-gen; \
  curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -; \
  curl https://packages.microsoft.com/config/debian/8/prod.list > /etc/apt/sources.list.d/mssql-release.list; \
  a2enmod headers proxy proxy_http ssl rewrite mpm_prefork; \
  a2dismod mpm_event; \
  apt-get update; \
  ACCEPT_EULA=Y apt-get install -y $BUILD_PACKAGES msodbcsql; \
  set +e; \
  docker-php-ext-install odbc; \
  set -e; \
  cd /usr/src/php/ext/odbc; \
  phpize; \
  sed -ri 's@^ *test +"\$PHP_.*" *= *"no" *&& *PHP_.*=yes *$@#&@g' configure; \
  ./configure --with-unixODBC=shared,/usr; \
  cd /root; \
  yes | pecl install ssh2-1.1.2 pdo_sqlsrv sqlsrv; \
  docker-php-ext-configure pdo_odbc --with-pdo-odbc=unixODBC,/usr; \ 
  docker-php-ext-install pdo_mysql mysqli zip pdo_odbc odbc; \
  docker-php-ext-enable ssh2 pdo_sqlsrv sqlsrv; \
  apt-get remove --purge -y $BUILD_PACKAGES && rm -rf /var/lib/apt/lists/*; \
  apt-get clean;
  
