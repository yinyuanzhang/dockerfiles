FROM centos:7

ENV INSTALL_PHP_VERSION="7.4.1"

# -- packages setup
RUN yum install -y epel-release
RUN yum update -y
RUN yum install -y \
        git \
        bzip2 \
        bzip2-devel \
        g++ gcc \
        libevent-devel \
        libxml2-devel \
        openssl-devel \
        libcurl-devel \
        libjpeg-devel \
        libpng-devel \
        re2c \
        libicu-devel \
        gcc-c++ \
        libmcrypt-devel \
        readline-devel \
        libtidy-devel \
        libxslt-devel \
        file \
        make \
        wget \
        autoconf \
        patch \
        bison \
        lemon \
        libsql \
        httpd-devel \
        mariadb-devel \
        postgresql-devel \
        freetype-devel \
        libc-client-devel \
        sqlite sqlite-devel \
        oniguruma oniguruma-devel \
        && rm -rf /var/cache/yum/* \
        && yum clean all

# -- for libzip 0.11
RUN yum install -y http://packages.psychotic.ninja/7/base/x86_64/RPMS/psychotic-release-1.0.0-1.el7.psychotic.noarch.rpm \
    && yum --enablerepo=psychotic-plus install -y libzip libzip-devel \
    && rm -rf /var/cache/yum/* \
    && yum clean all

# -- phpenv setup
RUN git clone https://github.com/riywo/anyenv ~/.anyenv \
    && echo 'export PATH="$HOME/.anyenv/bin:$PATH"' >> ~/.bashrc \
    && /root/.anyenv/bin/anyenv install --force-init \
    && echo 'eval "$(anyenv init -)"' >> ~/.bashrc \
    && . ~/.bashrc && anyenv install phpenv \
    && . ~/.bashrc && CONFIGURE_OPTS="--with-apxs2=/usr/bin/apxs --with-pdo-pgsql --with-pgsql --with-freetype-dir=/usr/include/freetype2/freetype --with-imap=/usr/lib64/ --with-imap-ssl" phpenv install -v $INSTALL_PHP_VERSION && \
    . ~/.bashrc && phpenv rehash

# -- copy modules & misc
RUN mkdir /root/.anyenv/envs/phpenv/versions/$INSTALL_PHP_VERSION/httpd_modules \
    && \cp -f /etc/httpd/modules/libphp*.so /root/.anyenv/envs/phpenv/versions/$INSTALL_PHP_VERSION/httpd_modules \
    && mkdir /root/.anyenv/envs/phpenv/versions/$INSTALL_PHP_VERSION/lib64_modules \
    && \cp -f /usr/lib64/libzip.so* /root/.anyenv/envs/phpenv/versions/$INSTALL_PHP_VERSION/lib64_modules \
    && \cp -f /usr/lib64/libonig.so* /root/.anyenv/envs/phpenv/versions/$INSTALL_PHP_VERSION/lib64_modules \
    && echo 'sendmail_path = /usr/sbin/sendmail -t -i' >> /root/.anyenv/envs/phpenv/versions/$INSTALL_PHP_VERSION/etc/php.ini

# -- staging
FROM busybox
COPY --from=0 /root/.anyenv/envs/phpenv/versions/$INSTALL_PHP_VERSION /root/.anyenv/envs/phpenv/versions/$INSTALL_PHP_VERSION
VOLUME /root/.anyenv/envs/phpenv/versions/$INSTALL_PHP_VERSION
