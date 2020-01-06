FROM ubuntu:16.04

RUN set -ex; \
	\
	apt-get update; \
	apt-get install -y --no-install-recommends nginx; \
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
    rm -rf /var/lib/apt/lists/*;

COPY  ./docker/web/conf.d/default.conf /etc/nginx/sites-available/default
RUN rm -rf /var/www
COPY ./src /var/www

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]