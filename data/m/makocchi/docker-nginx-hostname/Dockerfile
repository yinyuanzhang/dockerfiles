FROM alpine:3.9

RUN apk add -u --no-cache nginx nginx-mod-http-echo
RUN mkdir -p /run/nginx/ /usr/share/nginx/html

COPY files/etc/nginx/conf.d /etc/nginx/conf.d/

EXPOSE 80
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]

