FROM nginx:alpine
MAINTAINER SteamCache.Net Team <team@steamcache.net>

ENV GENERICCACHE_VERSION 1
ENV WEBUSER nginx
ENV CACHE_MEM_SIZE 500m
ENV CACHE_DISK_SIZE 500000m
ENV CACHE_MAX_AGE 3560d
ENV STEAMCACHE_DNS_VERSION 1

RUN	apk update			\
	&& apk add bind		\
	&& apk add sniproxy	

COPY overlay/ /

RUN	chmod 755 /scripts/*			;\
	mkdir -m 755 -p /data/cache		;\
	mkdir -m 755 -p /data/info		;\
	mkdir -m 755 -p /data/logs		;\
	mkdir -m 755 -p /tmp/nginx/		;\
	mkdir -p /var/cache/bind /var/log/named		\
	&& chmod 755 /scripts/*				\
	&& chown named:named /var/cache/bind /var/log/named ;\
	chown -R ${WEBUSER}:${WEBUSER} /data/	;\
	mkdir -p /etc/nginx/sites-enabled	;\
	ln -s /etc/nginx/sites-available/generic.conf /etc/nginx/sites-enabled/generic.conf

VOLUME ["/data/logs", "/data/cache", "/var/www"]

EXPOSE 80
EXPOSE 53/udp
EXPOSE 443

WORKDIR /scripts

ENTRYPOINT ["/scripts/bootstrap.sh"]
