FROM balenalib/raspberry-pi-alpine

RUN [ "cross-build-start" ]

RUN apk add --no-cache nginx \
	&& mkdir /run/nginx \
	&& ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

RUN [ "cross-build-end" ]

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
