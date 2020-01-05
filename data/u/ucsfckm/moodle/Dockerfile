FROM alpine/git as git
RUN apk update && apk add rsync
COPY . /moodle-git
RUN set -xe \
        && cd /moodle-git \
        && echo "COMMIT=$(git rev-parse HEAD)" > cle-release \
        && rsync -aq --exclude-from=./.gitignore \
                     --exclude=.git \
                     --exclude=.gitignore \
                     --exclude=.gitmodules \
                     --exclude=.gitattributes \
                     --exclude=Dockerfile \
                     --exclude=docker-compose.yml \
                     --exclude=docker-moodle-entrypoint \
                     --exclude=hooks/* \
                     ./ /moodle-html

FROM php:7.1-apache
#
# PHP extensions with no dependence
#
ENV PHP_EXT     mysqli opcache soap

#
# PHP extensions with dependence
#

# gd
ENV PHP_EXT     ${PHP_EXT} gd
ENV PHP_EXT_DEP libpng-dev libjpeg-dev libfreetype6-dev

# intl
ENV PHP_EXT     ${PHP_EXT} intl
ENV PHP_EXT_DEP ${PHP_EXT_DEP} libicu-dev

# ldap
ENV PHP_EXT     ${PHP_EXT} ldap
ENV PHP_EXT_DEP ${PHP_EXT_DEP} libldap2-dev

# xmlrpc
ENV PHP_EXT     ${PHP_EXT} xmlrpc
ENV PHP_EXT_DEP ${PHP_EXT_DEP} libxml2-dev

# zip
ENV PHP_EXT     ${PHP_EXT} zip
ENV PHP_EXT_DEP ${PHP_EXT_DEP} zlib1g-dev

#
# Install PHP extensions
#
RUN set -xe \
        && apt-get update && apt-get install -y ${PHP_EXT_DEP} --no-install-recommends \
        && echo "Configure GD extension" \
        && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
        && echo "Configure LDAP extension" \
        && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
        && docker-php-ext-install -j$(nproc) ${PHP_EXT} \
        && apt-get remove --purge -y ${PHP_EXT_DEP} \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

#
# Copy moodle source to work directory
#
COPY --from=git /moodle-html .

#
# Create directory for moodledata
#
RUN set -xe && mkdir -p /var/www/moodledata

#
# Copy and override php entrypoint with docker-moodle-entrypoint
#
COPY --from=git /moodle-git/docker-moodle-entrypoint /usr/local/bin/

ENTRYPOINT ["docker-moodle-entrypoint"]
CMD ["apache2-foreground"]
