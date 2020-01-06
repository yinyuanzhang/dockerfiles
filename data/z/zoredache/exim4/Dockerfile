# inspired from https://github.com/tianon/dockerfiles/tree/master/exim4

FROM debian:buster-slim

RUN set -eux; \
  apt-get update; \
  adduser \
    --system --group --quiet --home /var/spool/exim4 --uid 110 \
    --no-create-home --disabled-login --force-badname Debian-exim ; \
  </dev/null DEBIAN_FRONTEND=noninteractive \
  apt-get install --yes --no-install-recommends \
    tini exim4-daemon-light; \
  rm -rf /var/lib/apt/lists/*; \
  ln -svfT /etc/hostname /etc/mailname

RUN set -eux; \
	mkdir -p /var/spool/exim4 /var/log/exim4; \
	chown -R Debian-exim:Debian-exim /var/spool/exim4 /var/log/exim4
VOLUME ["/var/spool/exim4", "/var/log/exim4"]

COPY docker-entrypoint.sh /usr/local/bin/
COPY update-exim4.conf.conf /etc/exim4/

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 25
CMD ["tini", "--", "exim", "-bd", "-v"]

