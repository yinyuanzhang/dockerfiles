FROM joomla:3.9.10
LABEL maintainer="Cienrxs"

RUN set -ex; \
	\
	apt-get update; \
	apt-get install -y --no-install-recommends \
		php-common/stable \
		php-phpseclib/stable \
	; \
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
	rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/entrypoint.sh"]
CMD ["apache2-foreground"]
