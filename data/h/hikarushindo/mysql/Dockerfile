FROM hikarushindo/alpine:3.5

MAINTAINER Pascal Nitsche

ENV MYSQL_MAJOR 5.5
ENV MYSQL_VERSION 5.5.54
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/mysql/bin:/usr/local/mysql/scripts

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN addgroup -S mysql && adduser -S -G mysql mysql

RUN mkdir /docker-entrypoint-initdb.d && \
    \
    # For entrypoint to work
    apk add --no-cache bash su-exec && \
    # FATAL ERROR: please install the following Perl modules before executing /usr/local/mysql/scripts/mysql_install_db:
    # File::Basename
    # File::Copy
    # Sys::Hostname
    # Data::Dumper
    apk add --no-cache perl && \
    # mysqld: error while loading shared libraries: libaio.so.1: cannot open shared object file: No such file or directory
    apk add --no-cache libaio pwgen && \
    # mysqld: error could not load libstdc++.so
    apk add --no-cache libstdc++ && \
    # mysqld: There were fatal errors during processing of zoneinfo directory
    apk add --no-cache tzdata

RUN apk add --no-cache --virtual .build-deps cmake build-base wget gnupg tar ca-certificates git binutils debian-archive-keyring ncurses-dev && \
    update-ca-certificates && \
    wget "https://cdn.mysql.com/Downloads/MySQL-$MYSQL_MAJOR/mysql-$MYSQL_VERSION.tar.gz" -O mysql.tar.gz  && \
    wget "https://cdn.mysql.com/Downloads/MySQL-$MYSQL_MAJOR/mysql-$MYSQL_VERSION.tar.gz.asc" -O mysql.tar.gz.asc && \
    export GNUPGHOME="$(mktemp -d)" && \
    # gpg: key 5072E1F5: public key "MySQL Release Engineering <mysql-build@oss.oracle.com>" imported
     gpg --keyserver ha.pool.sks-keyservers.net --recv-keys A4A9406876FCBD3C456770C88C718D3B5072E1F5 && \
     gpg --batch --verify mysql.tar.gz.asc mysql.tar.gz && \
     rm -r "$GNUPGHOME" mysql.tar.gz.asc && \
    mkdir -p mysqlsrc && \
    tar -xzf mysql.tar.gz -C mysqlsrc --strip-components=1 && \
    mkdir build && \
    cd build && \
    cmake ../mysqlsrc && \
    make && \
    make install && \
    cd .. && \
    rm -rf build mysqlsrc && \
    rm mysql.tar.gz && \
    mkdir -p /usr/local/mysql && \
    rm -rf /usr/local/mysql/mysql-test /usr/local/mysql/sql-bench && \
    rm -rf /usr/local/mysql/bin/*-debug /usr/local/mysql/bin/*_embedded && \
    chmod +x /usr/local/mysql/bin/* && \
    find /usr/local/mysql -type f -name "*.a" -delete && \
    { find /usr/local/mysql -type f -executable -exec strip --strip-all '{}' + || true; } && \
    mkdir -p /etc/mysql/conf.d && \
    { \
      echo '[mysqld]'; \
      echo 'skip-host-cache'; \
      echo 'skip-name-resolve'; \
      echo 'datadir = /var/lib/mysql'; \
      echo '!includedir /etc/mysql/conf.d/'; \
    } > /etc/mysql/my.cnf && \
    mkdir -p /var/lib/mysql /var/run/mysqld && \
    chown -R mysql:mysql /var/lib/mysql /var/run/mysqld && \
    # ensure that /var/run/mysqld (used for socket and lock files) is writable regardless of the UID our mysqld instance ends up having at runtime
    chmod 777 /var/run/mysqld && \
    rm -rf *.tar.gz* /usr/src /root/.gnupg && \
    apk del .build-deps

VOLUME /var/lib/mysql

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 3306
CMD ["mysqld"]
