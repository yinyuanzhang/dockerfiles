FROM nginx:alpine

RUN set -ex \
	&& apk add --no-cache apache2-utils \
	&& rm -Rf /tmp/*
#	&& cp /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.orig

COPY WampShark /usr/share/nginx/html
COPY nginx_bootstrap.sh /usr/bin/

ENV WAMP_REALM=realm1
ENV WAMP_ROUTER_URI=ws://router:1111/ws
ENV AUTH_USERNAME=admin
ENV AUTH_PASSWORD=1234

ENTRYPOINT nginx_bootstrap.sh
