FROM haproxy:alpine

RUN apk add --no-cache \
	bash \
	ca-certificates \
	inotify-tools

COPY docker-entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]

