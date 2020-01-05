FROM nginx:alpine
MAINTAINER SteamCache.Net Team <team@steamcache.net>

ENV GENERICCACHE_VERSION 1
ENV WEBUSER nginx

COPY overlay/ /

RUN	chmod 755 /scripts/*			;\
	mkdir -m 755 -p /data/cache		;\
	mkdir -m 755 -p /data/info		;\
	mkdir -m 755 -p /data/logs		;\
	mkdir -m 755 -p /tmp/nginx/		;\
	chown -R ${WEBUSER}:${WEBUSER} /data/	;\
	mkdir -p /etc/nginx/sites-enabled	;\
	ln -s /etc/nginx/sites-available/generic.conf /etc/nginx/sites-enabled/generic.conf

VOLUME ["/data/logs", "/data/cache", "/var/www"]

EXPOSE 80

WORKDIR /scripts

ENTRYPOINT ["/scripts/bootstrap.sh"]
