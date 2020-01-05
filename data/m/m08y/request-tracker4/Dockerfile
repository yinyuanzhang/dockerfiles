FROM debian:buster-slim

LABEL maintainer="Aneurin Price adp@nyeprice.space"

RUN set -eux; \
  export DEBIAN_FRONTEND=noninteractive; \
  apt-get update; \
  apt-get install -y --no-install-recommends \
    curl \
    fetchmail \
    libdatetime-event-ical-perl \
    libdbd-mysql-perl \
    libdbd-pg-perl \
    libdbix-searchbuilder-perl \
    libemail-sender-perl \
    libhook-lexwrap-perl \
    libhtml-formatexternal-perl \
    msmtp \
    perl-doc \
    procps \
    request-tracker4 \
    rrdtool \
    rt4-db-sqlite \
    rt4-standalone \
    starman \
    supervisor \
    w3m \
  ; \
  ( cd /etc/request-tracker4/RT_SiteConfig.d/; rm \
    50-debconf.pm \
    51-dbconfig-common.pm \
    60-logging.pm \
  ); \
  chmod g+r /etc/request-tracker4/RT_SiteConfig.pm; \
  chgrp www-data /etc/request-tracker4/RT_SiteConfig.pm; \
  ln -s /usr/share/request-tracker4/libexec/rt-server /usr/local/bin; \
  find /var/lib/apt/lists -mindepth 1 -delete; \
  rm -rf /etc/request-tracker4

###
### Supercronic for unprivileged crontabs in containers ###
# https://github.com/aptible/supercronic/releases/latest

ARG SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/v0.1.9/supercronic-linux-amd64
ARG SUPERCRONIC=supercronic-linux-amd64
ARG SUPERCRONIC_SHA1SUM=5ddf8ea26b56d4a7ff6faecdd8966610d5cb9d85

RUN curl -fsSLO "$SUPERCRONIC_URL" \
 && echo "${SUPERCRONIC_SHA1SUM}  ${SUPERCRONIC}" | sha1sum -c - \
 && chmod +x "$SUPERCRONIC" \
 && mv "$SUPERCRONIC" "/usr/local/bin/${SUPERCRONIC}" \
 && ln -s "/usr/local/bin/${SUPERCRONIC}" /usr/local/bin/supercronic && mkdir /var/www && chown www-data:www-data /var/www -R
###

COPY entrypoint /
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY --chown=www-data:www-data etc/request-tracker4/ /etc/request-tracker4
COPY etc/cron.d/ /etc/cron.d

EXPOSE 8080

USER www-data

CMD /entrypoint; /usr/bin/supervisord

HEALTHCHECK CMD --interval=2m curl http://localhost:8080|grep Best\ Practical||echo "Could not start, usually a database error, consult logs" && exit 1 

# vim: ts=2 sw=2 et sts=2 ft=dockerfile
