FROM mparker17/drupal7

# Setup the Xdebug version to install.
ENV XDEBUG_VERSION 2.4.0
ENV XDEBUG_SHA1 a9bc9c6b9e8bc913fb1f7c6f6d19f6222d430414

# Install Xdebug.
RUN set -x && \
    curl -SL "http://www.xdebug.org/files/xdebug-$XDEBUG_VERSION.tgz" -o xdebug.tgz && \
    echo $XDEBUG_SHA1 xdebug.tgz | shasum -a 1 - && \
    mkdir -p /usr/src/xdebug && \
    tar -xf xdebug.tgz -C /usr/src/xdebug --strip-components=1 && \
    rm xdebug.* && \
    cd /usr/src/xdebug && \
    phpize && \
    ./configure && \
    make -j"$(nproc)" && \
    make install && \
    make clean

ADD ext-xdebug.ini /usr/local/etc/php/conf.d/
