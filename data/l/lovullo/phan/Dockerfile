FROM phpqa/phan:latest

# Install extra extensions
RUN set -ex; \
    docker-php-source extract; \
    { \
        echo '# https://github.com/docker-library/php/issues/103#issuecomment-271413933'; \
        echo 'AC_DEFUN([PHP_ALWAYS_SHARED],[])dnl'; \
        echo; \
        cat /usr/src/php/ext/odbc/config.m4; \
    } > temp.m4; \
    mv temp.m4 /usr/src/php/ext/odbc/config.m4; \
    apk --update add openldap-dev unixodbc-dev zlib-dev; \
    docker-php-ext-configure odbc --with-unixODBC=shared,/usr; \
    docker-php-ext-install ldap mysqli odbc zip; \
    docker-php-source delete;

