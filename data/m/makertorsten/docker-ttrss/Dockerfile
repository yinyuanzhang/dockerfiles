# Using https://github.com/gliderlabs/docker-alpine
# plus  https://github.com/just-containers/s6-overlay for a s6 Docker overlay.
FROM alpine
# Initialy was based on work of Christian Lück <christian@lueck.tv>
LABEL description="A complete, self-hosted Tiny Tiny RSS (TTRSS) environment." \
      maintainer="Torsten Enkelmann <t.enkelmann@web.de>"

RUN set -xe && apk update && apk upgrade
RUN set -xe && apk add --update --no-cache --virtual=run-deps shadow busybox nginx git ca-certificates curl bash tar git
RUN set -xe && apk add --update --no-cache --virtual build-dependencies
RUN set -xe && apk add php7 php7-fpm php7-cli php7-curl php7-dom php7-gd php7-iconv php7-fileinfo php7-json php7-mcrypt php7-pgsql php7-pcntl php7-pdo php7-pdo_pgsql php7-mysqli php7-pdo_mysql php7-mbstring php7-posix php7-session

# Add user www-data for php-fpm.
# 82 ist the standard uid/gid for "www-data" in Alpine.
# RUN set -xe && groupadd -g 82 www-data
RUN set -xe && adduser -u 82 -D -S -G www-data www-data

# Copy root file system.
COPY root /
RUN chmod +x /srv/*.sh

# install ttrss and patch configuration
WORKDIR /var/www
RUN set -xe && mkdir plugins.local
RUN set -xe && mkdir themes.local
RUN set -xe && curl -SL https://git.tt-rss.org/git/tt-rss/archive/master.tar.gz | tar xzC /var/www --strip-components 1
RUN set -xe && apk del build-dependencies
RUN set -xe && cp config.php-dist config.php
RUN set -xe && chown -R www-data:www-data /var/www

# install ttrss themes and plugins
WORKDIR /var/www
RUN set -xe && git clone --depth=1 https://github.com/sepich/tt-rss-mobilize.git /var/www/plugins.local/mobilize
RUN set -xe && git clone --depth=1 https://github.com/m42e/ttrss_plugin-feediron.git /var/www/plugins.local/feediron
RUN set -xe && git clone --depth=1 https://github.com/levito/tt-rss-feedly-theme.git /var/www/themes.local/levito-feedly-git
RUN set -xe && git clone --depth=1 https://github.com/Gravemind/tt-rss-feedlish-theme.git /var/www/themes.local/gravemind-feedly-git

# Add s6 overlay.
# Note: Tweak this line if you're running anything other than x86 AMD64 (64-bit).
RUN curl -L -s https://github.com/just-containers/s6-overlay/releases/download/v1.22.1.0/s6-overlay-amd64.tar.gz | tar xvzf - -C /

# Add wait-for-it.sh
ADD https://raw.githubusercontent.com/Eficode/wait-for/master/wait-for /srv
RUN chmod 755 /srv/wait-for

# Expose Nginx ports.
EXPOSE 80
# EXPOSE 4443

# Expose default database credentials via ENV in order to ease overwriting.
ENV DB_NAME ttrss
ENV DB_USER ttrss
ENV DB_PASS ttrss

# Clean up.
RUN set -xe && apk del --progress --purge && rm -rf /var/cache/apk/*

ENTRYPOINT ["/init"]
