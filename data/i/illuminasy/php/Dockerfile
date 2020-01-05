# Illuminasy PHP Docker
#
# VERSION               1.1.0

FROM illuminasy/php:latest-dev

LABEL Description="This image contains php with dev tools."
LABEL Vendor="Illuminasy"
LABEL Version="1.1.0"
LABEL maintainer="Abhishek Salian <abhi@illuminasy.com>"
LABEL com.illuminasy.php.version="1.1.0"
LABEL com.illuminasy.php.release-date="2019-12-17"
LABEL com.illuminasy.php.version.is-production="false"

# Copy monitoring tools
COPY ./monitoring_tools /opt/monitoring_tools

USER root

RUN apk add --update --no-cache openrc \
    && mkdir -p /run/openrc /var/log/newrelic \
    && touch /run/openrc/softlevel \
    && chown -R illuminasy:www-data /var/log/newrelic \
    && cd /opt/monitoring_tools/newrelic-php5-9.4.0.249-linux-musl \
    && NR_INSTALL_SILENT=true ./newrelic-install install \
    && sed -i '/newrelic.license = /c\newrelic.license = ${NEWRELIC_KEY}' /usr/local/etc/php/conf.d/newrelic.ini \
    && sed -i '/newrelic.appname = /c\newrelic.appname = "${NEWRELIC_APPNAME}"' /usr/local/etc/php/conf.d/newrelic.ini

USER illuminasy
