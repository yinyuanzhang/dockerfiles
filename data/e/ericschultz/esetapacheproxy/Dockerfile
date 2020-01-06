FROM alpine:3.8

RUN apk add --no-cache apache2 apache2-proxy apache2-ssl

COPY entrypoint.sh /sbin

RUN mkdir -p /httpd-conf/logs
COPY httpd.conf /httpd-conf/
RUN ln -s /usr/lib/apache2 /httpd-conf/modules

CMD [ "/sbin/entrypoint.sh" ]

