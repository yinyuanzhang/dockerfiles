FROM alpine

RUN apk add --update \
    apache2 \
&&  rm -rf /var/cache/apk/*

RUN mkdir -p /run/apache2

CMD /usr/sbin/httpd -DFOREGROUND
