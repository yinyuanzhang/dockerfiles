ARG ALPINE_VERSION=latest

FROM alpine:${ALPINE_VERSION}
LABEL maintainer="dekart811" \
	com.nginx-rtmp.description="Alpine based nginx with the rtmp module for live multimedia streaming."

RUN apk add --no-cache tzdata nginx nginx-mod-rtmp &&\
	mkdir -p /run/nginx &&\
	ln -sf /dev/stdout /var/log/nginx/access.log &&\
	ln -sf /dev/stderr /var/log/nginx/error.log

ADD ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 1935

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]
