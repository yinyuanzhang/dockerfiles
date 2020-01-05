FROM owncloud/base:xenial

LABEL maintainer="ownCloud DevOps <devops@owncloud.com>" \
  org.label-schema.name="ownCloud Server" \
  org.label-schema.vendor="ownCloud GmbH" \
  org.label-schema.schema-version="1.0"

RUN curl -L -o /var/www/owncloud-10.0.10.tar.bz2 https://download.owncloud.org/community/owncloud-10.0.10.tar.bz2
RUN mkdir -p /var/www/owncloud/apps ; curl -L -o /var/www/owncloud/apps/user_ldap.tar.gz https://github.com/owncloud/user_ldap/releases/download/v0.11.0/user_ldap.tar.gz

RUN find /var/www/owncloud \( \! -user www-data -o \! -group www-data \) -print0 | xargs -r -0 chown www-data:www-data
